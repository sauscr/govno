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
    
    result = serializers.ReadOnlyField()
    percentage_deviation = serializers.ReadOnlyField()

    class Meta:
        model = TableOne
        fields = [
            'actual_value',
            'diff_reason',
            'init',
            'percentage_deviation'
        ]


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
