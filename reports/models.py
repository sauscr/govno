from django.db import models
import re


class TableOne(models.Model):
    """Модель для таблицы 1"""
    actual_value = models.FloatField(
        verbose_name='Значение на конец отчетного периода',
        )
    diff_reason = models.CharField(
        max_length=255,
        verbose_name='Обоснование отклонения фактического значения',
        )
    init = models.ForeignKey('InitialData', on_delete=models.CASCADE, null=True)

    @property
    def get_result(self):
        """
        Метод, связанный с определением результата работы
        
        - plan_value: запланированное значение, поле модели InitialData
        - actual_value: фактическое значение, поле модели TableOne
        """
        plan_value = self.init.plan_value
        actual_value = self.actual_value
        if plan_value > actual_value:
            return 'Не достигнут'
        return 'Достигнут'
    
    @property
    def get_calculate_relative_deviation(self):
        """
        Метод, связанный с определением % выполнения работы
        
        - plan_value: запланированное значение, поле модели InitialData
        - actual_value: фактическое значение, поле модели TableOne
        """
        plan_value = self.init.plan_value
        actual_value = self.actual_value
        if plan_value is not None and actual_value != 0:
            return round(abs(
                ((plan_value - actual_value) / plan_value) * 100
                ), 2)
        return None


class TableTwo(models.Model):
    """Модель для тыблицы 2"""
    rf_actually = models.FloatField(verbose_name='Референс', null=True)
    rb_actually = models.FloatField(verbose_name='РБ', null=True)
    mb_actually = models.FloatField(verbose_name='МБ', null=True)
    vnb_actually = models.FloatField(verbose_name='ВНБ', null=True)
    init = models.ForeignKey('InitialData', on_delete=models.CASCADE, null=True)

    @property
    def get_planned_sum(self):
        """
        Вычисление суммы плановых значений.
        
        - rf_set: запланированное значение, поле модели InitialData
        - rb_set: запланированное значение, поле модели InitialData
        - mb_set: запланированное значение, поле модели InitialData
        - vnb_set: запланированное значение, поле модели InitialData
        """
        rf_set = self.init.rf_set
        rb_set = self.init.rb_set
        mb_set = self.init.mb_set
        vnb_set = self.init.vnb_set
        return sum([
            rf_set,
            rb_set,
            mb_set,
            vnb_set
        ])

    @property
    def get_actual_sum(self):
        """
        Вычисление суммы фактических значений.
        
        - rf_actually: фактическое значение, поле модели TableTwo
        - rb_actually: фактическое значение, поле модели TableTwo
        - mb_actually: фактическое значение, поле модели TableTwo
        - vnb_actually: фактическое значение, поле модели TableTwself
        """
        return sum([
            self.rf_actually,
            self.rb_actually,
            self.mb_actually,
            self.vnb_actually,
        ])
    
    @property
    def get_calculate_ratio_mastered_to_unmastered(self):
        pass


class TableThree(models.Model):
    """Модель для таблицы 3"""
    time_execution_actually = models.FloatField(verbose_name='Время по факту',)
    actual_result = models.CharField(max_length=255, verbose_name='Результат',)
    init = models.ForeignKey('InitialData', on_delete=models.CASCADE, null=True)

    @property
    def get_executor(self):
        """
        Поиска текста между двойными кавычками в строке.
        

        """
        text = self.init.event_name
        pattern = r'«(.*?)»'
        much = re.search(pattern, text)
        if much:
            return much.group(1)
        return None

    @property
    def get_result(self):
        """
        Методы, связанные с определением результатов.
        

        """
        time_execution_actually = self.time_execution_actually
        time_execution_plan = self.init.time_execution_plan
        if time_execution_actually > time_execution_plan:
            return 'Не достигнут'
        else:
            return 'Достигнут'

    @property
    def get_percent(self):
        """
        Вычисление процента выполнения задачи.


        """
        time_execution_actually = self.time_execution_actually
        time_execution_plan = self.init.time_execution_plan
        if time_execution_actually is not None and time_execution_plan != 0:
            return round((time_execution_actually / time_execution_plan) * 100, 2)
        return None


class InitialData(models.Model):
    """Модель для инициализации данных"""
    indicator_name = models.CharField(
        max_length=255,
        verbose_name='Наименование целевого индикатора',
        )
    unit = models.CharField(
        max_length=50,
        verbose_name='Единица измерения',
        )
    plan_value = models.FloatField(verbose_name='План на текущий год')

    event_name = models.CharField(
        max_length=255,
        verbose_name='Наименование мероприятия',
        )
    rf_set = models.FloatField(verbose_name='Референс',)
    rb_set = models.FloatField(verbose_name='РБ',)
    mb_set = models.FloatField(verbose_name='МБ',)
    vnb_set = models.FloatField(verbose_name='ВНБ',)

    time_execution_plan = models.FloatField(verbose_name='Срок выполнения по плану',)
    expected_result = models.CharField(max_length=255, verbose_name='Ожидаемы результат',)
