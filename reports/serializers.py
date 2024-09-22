from rest_framework import serializers
from .models import InitialData, TableOne, TableTwo, TableThree
import re


class InitialDataSerializer(serializers.ModelSerializer):
    '''
    Сериализатор для модели InitialData.

    Этот сериализатор используется для преобразования данных модели InitialData 
    в формат JSON и обратно.
    '''
    class Meta:
        model = InitialData
        fields = [
            'indicator_name',
            'unit',
            'plan_value',
            'event_name',
            'rf_set',
            'rb_set',
            'mb_set',
            'vnb_set',
            'time_execution_plan',
            'expected_result',
        ]


class TableOneSerializer(serializers.ModelSerializer):
    '''
    Сериализатор для модели TableOne.

    Этот сериализатор дополнительно включает вычисляемые поля:
        - result: Показывает, достигнуто ли плановое значение.
        - calculate_relative_deviation: Вычисляет относительную
        дивергенцию между фактическим и плановым значением.
    '''
    result = serializers.SerializerMethodField()
    calculate_relative_deviation = serializers.SerializerMethodField()
    class Meta:
        model = TableOne
        fields = [
            'actual_value',
            'diff_reason',
            'init',
            'result',
            'calculate_relative_deviation',
        ]

    def get_result(self, obj):
        '''Методы, связанные с определением результатов.'''
        plan_value = obj.init.plan_value
        actual_value = obj.actual_value
        if plan_value > actual_value:
            return 'Не достигнут'
        else:
            return 'Достигнут'
        
    def get_calculate_relative_deviation(self, obj):
        '''Вычисление относительной дивергенции между двумя значениями.'''
        plan_value = obj.init.plan_value
        actual_value = obj.actual_value
        if plan_value is not None and actual_value != 0:
            return round(abs(((plan_value - actual_value) / plan_value) * 100), 2)
        return None


class TableTwoSerializer(serializers.ModelSerializer):
    '''
    Сериализатор для модели TableTwo.

    Этот сериализатор включает вычисляемые поля:
        - planned_sum/get_planned_sum: Сумма плановых значений по набору.
        - actual_sum/get_actual_sum: Сумма фактических значений по набору.
    '''
    planned_sum = serializers.SerializerMethodField()
    actual_sum = serializers.SerializerMethodField()
    # calculate_ratio_mastered_to_unmastered = serializers.SerializerMethodField() это пока не работает)

    class Meta:
        model = TableTwo
        fields = [
            'rf_actually',
            'rb_actually',
            'mb_actually',
            'vnb_actually',
            'init',
            'planned_sum',
            'actual_sum',
            # 'calculate_ratio_mastered_to_unmastered', это тоже
        ]

    def get_planned_sum(self, obj):
        '''Вычисление суммы плановых значений.'''
        rf_set = obj.init.rf_set
        rb_set = obj.init.rb_set
        mb_set = obj.init.mb_set
        vnb_set = obj.init.vnb_set
        return sum([
            rf_set,
            rb_set,
            mb_set,
            vnb_set
        ])

    def get_actual_sum(self, obj):
        '''Вычисление суммы фактических значений.'''
        return sum([
            obj.rf_actually,
            obj.rb_actually,
            obj.mb_actually,
            obj.vnb_actually,
        ])

    # def get_calculate_ratio_mastered_to_unmastered(self, obj):
    #     actual_sum = obj.actual_sum
    #     planned_sum = obj.planned_sum
    #     if actual_sum is not None and planned_sum != 0:
    #         return round((actual_sum / planned_sum) * 100, 2)
    #     return None          и это тоже не работает


class TableThreeSerializer(serializers.ModelSerializer):
    '''
    Сериализатор для модели TableThree.

    Этот сериализатор включает вычисляемые поля:
        - executor/get_executor: Извлекает имя исполнителя из строки event_name (из " ").
        - result/get_result: Определяет, достигнута ли цель на основе времени выполнения.
        - percent/get_percent: Процент выполнения по сравнению с планом.
    '''
    executor = serializers.SerializerMethodField()
    result = serializers.SerializerMethodField()
    percent = serializers.SerializerMethodField()

    class Meta:
        model = TableThree
        fields = [
            'time_execution_actually',
            'actual_result',
            'init',
            'executor',
            'result',
            'percent',
        ]

    def get_executor(self, obj):
        '''Поиска текста между двойными кавычками в строке.'''
        text = obj.init.event_name
        pattern = r'«(.*?)»'
        much = re.search(pattern, text)
        if much:
            return much.group(1)
        return None

    def get_result(self, obj):
        '''Методы, связанные с определением результатов.'''
        time_execution_actually = obj.time_execution_actually
        time_execution_plan = obj.init.time_execution_plan
        if time_execution_actually > time_execution_plan:
            return 'Не достигнут'
        else:
            return 'Достигнут'

    def get_percent(self, obj):
        '''Вычисление процента выполнения задачи.'''
        time_execution_actually = obj.time_execution_actually
        time_execution_plan = obj.init.time_execution_plan
        if time_execution_actually is not None and time_execution_plan != 0:
            return round((time_execution_actually / time_execution_plan) * 100, 2)
        return None

