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
    result = serializers.CharField(source='get_result', read_only=True)
    calculate_relative_deviation = serializers.FloatField(
        source='get_calculate_relative_deviation',
        read_only=True,
        )

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
    planned_sum = serializers.FloatField(
        source='get_planned_sum',
        read_only=True,
        )
    actual_sum = serializers.FloatField(
        source='get_actual_sum',
        read_only=True,
        )

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
        ]


class TableThreeSerializer(serializers.ModelSerializer):
    executor = serializers.CharField(source='get_executor', read_only=True)
    result = serializers.CharField(source='get_result', read_only=True)
    percent = serializers.FloatField(source='get_percent', read_only=True)

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
