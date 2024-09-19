from django.db import models
from services.logic_services import *

class TableOne(models.Model):

    actual_value = models.FloatField(verbose_name=
                                     'Значение на конец отчетного периода',)
    diff_reason = models.CharField(max_length=255,
                                   verbose_name=
                                   'Обоснование отклонения фактического значения',)
    
    init = models.ForeignKey('InitialData', on_delete=models.CASCADE, null=True)

    @property
    def result(self):
        plan_value = self.init.plan_value
        return result(
            plan_value,
            self.actual_value)
    
    @property
    def percentage_deviation(self):
        plan_value = self.init.plan_value
        return calculate_relative_diviation(plan_value,
                                             self.actual_value)


class TableTwo(models.Model):

    rf_actually = models.FloatField(verbose_name='Референс', null=True)
    rb_actually = models.FloatField(verbose_name='РБ', null=True)
    mb_actually = models.FloatField(verbose_name='МБ', null=True)
    vnb_actually = models.FloatField(verbose_name='ВНБ', null=True)

    init = models.ForeignKey('InitialData', on_delete=models.CASCADE, null=True)

    @property
    def planned_sum(self):
        rf_set = self.init.rf_set
        rb_set = self.init.rb_set
        mb_set = self.init.mb_set
        vnb_set = self.init.vnb_set
        return sum([rf_set, rb_set, mb_set, vnb_set])

    @property
    def actual_sum(self):
        return sum([
            self.rf_actually, self.rb_actually, self.mb_actually, self.vnb_actually
        ])


    @property
    def percent(self):
        return calculate_ratio_mastered_to_unmastered(
            self.actual_sum, self.planned_sum
        )

class TableThree(models.Model):

    time_execution_actually = models.FloatField(verbose_name='Время по факту',)
    actual_result = models.CharField(max_length=255, verbose_name='Результат',)

    init = models.ForeignKey('InitialData', on_delete=models.CASCADE, null=True)

    @property
    def executor(self):
        text = self.init.indicator_name
        return extract_text(text)

    @property
    def result(self):
        plan = self.init.time_execution_plan
        return result(
            self.time_execution_actually, plan
        )


    @property
    def percent(self):
        plan = self.init.time_execution_plan
        return calculate_ratio_mastered_to_unmastered(
            plan, self.time_execution_actually
        )



class InitialData(models.Model):

    indicator_name = models.CharField(max_length=255,
                                      verbose_name='Наименование целевого индикатора')
    unit = models.CharField(max_length=50,
                            verbose_name='Единица измерения')
    plan_value = models.FloatField(verbose_name='План на текущий год')


    event_name = models.CharField(max_length=255,
                                  verbose_name='Наименование мероприятия',)
    rf_set = models.FloatField(verbose_name='Референс',)
    rb_set = models.FloatField(verbose_name='РБ',)
    mb_set = models.FloatField(verbose_name='МБ',)
    vnb_set = models.FloatField(verbose_name='ВНБ',)


    time_execution_plan = models.FloatField(verbose_name='Срок выполнения по плану',)
    expected_result = models.CharField(max_length=255, verbose_name='Ожидаемы результат',)
