from rest_framework import serializers
from reports.models import InitialData, TableOne, TableTwo, TableThree


class InitialDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = InitialData
        fields = '__all__'


class TableOneSerializer(serializers.ModelSerializer):

    init = InitialDataSerializer(read_only=True)
    
    result = serializers.ReadOnlyField()
    percentage_deviation = serializers.ReadOnlyField()

    class Meta:
        model = TableOne
        fields = [
            'actual_value', 'diff_reason', 'init',
            'result', 'percentage_deviation'
        ]


class TableTwoSerializer(serializers.ModelSerializer):

    init = InitialDataSerializer(read_only=True)
    
    planned_sum = serializers.ReadOnlyField()
    actual_sum = serializers.ReadOnlyField()
    percent = serializers.ReadOnlyField()

    class Meta:
        model = TableTwo
        fields = [
            'rf_actually', 'rb_actually', 'mb_actually',
            'vnb_actually', 'init', 'planned_sum',
            'actual_sum', 'percent'
        ]

class TableThreeSerializer(serializers.ModelSerializer):

    init = InitialDataSerializer(read_only=True)
    
    executor = serializers.ReadOnlyField()
    result = serializers.ReadOnlyField()
    percent = serializers.ReadOnlyField()

    class Meta:
        model = TableThree
        fields = [
            'time_execution_actually', 'actual_result',
            'init', 'executor', 'result', 'percent'
        ]
