from rest_framework import serializers
from .models import InitialData, TableOne, TableTwo, TableThree


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
