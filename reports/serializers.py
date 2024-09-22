from rest_framework import serializers
from .models import InitialData, TableOne, TableTwo, TableThree


class InitialDataSerializer(serializers.ModelSerializer):
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

    init = InitialDataSerializer(read_only=True)
    
    planned_sum = serializers.ReadOnlyField()
    actual_sum = serializers.ReadOnlyField()
    percent = serializers.ReadOnlyField()

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
            'percent',
        ]

class TableThreeSerializer(serializers.ModelSerializer):

    init = InitialDataSerializer(read_only=True)
    
    executor = serializers.ReadOnlyField()
    result = serializers.ReadOnlyField()
    percent = serializers.ReadOnlyField()

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
