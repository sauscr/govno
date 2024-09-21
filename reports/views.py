from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets

from .models import InitialData, TableOne, TableTwo, TableThree, InitialData
from .serializers import InitialDataSerializer,\
    TableOneSerializer, TableTwoSerializer, TableThreeSerializer



class InitialDataViewSet(viewsets.ModelViewSet):
    queryset = InitialData.objects.all()
    serializer_class = InitialDataSerializer

class TableOneViewSet(viewsets.ModelViewSet):
    queryset = TableOne.objects.all()
    serializer_class = TableOneSerializer

class TableTwoViewSet(viewsets.ModelViewSet):
    queryset = TableTwo.objects.all()
    serializer_class = TableTwoSerializer

class TableThreeViewSet(viewsets.ModelViewSet):
    queryset = TableThree.objects.all()
    serializer_class = TableThreeSerializer


class DataAPIView(APIView):
    '''
    Универсальный APIView для таблиц
    '''
    model = None
    serializer_class = None
    initial_fields = []
    table_fields = []
    
    def get(self, request):
        values = InitialData.objects.values(*self.initial_fields)
        table_data = self.model.objects.values(*self.table_fields)

        combined_data =[
            {**init, **table} for init, table in zip(values, table_data)
        ]
        return Response(combined_data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class InitialDataView(DataAPIView):
    '''
    API для InitialData
    '''
    model = InitialData
    serializer_class = InitialDataSerializer


class TableOneAPIView(DataAPIView):

    model = TableOne
    serializer_class = InitialDataSerializer
    initial_fields = [
        'indicator_name',
        'unit',
        'plan_value',
    ]
    table_fields = [
        'actual_value',
        'result',
        'percentage_deviation',
    ]


class TableTwoAPIView(DataAPIView):

    model = TableTwo
    serializer_class = InitialDataSerializer
    initial_fields = [
        'event_name',
        'rf_set',
        'rb_set',
        'mb_set',
        'vnb_set',
    ]
    table_fields = [
        'rf_actually',
        'rb_actually',
        'mb_actually',
        'vnb_actually',
        'planned_sum',
        'actual_sum',
        'percent',
    ]


class TableThreeAPIView(DataAPIView):

    model = TableThree
    serializer_class = InitialDataSerializer
    initial_fields = [
        'event_name',
        'expected_result',
        'time_execution_plan',
    ]
    table_fields = [
        'actual_result',
        'time_execution_actually ',
        'executor',
        'result',
        'percent',
    ]
