from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets, mixins

from .models import InitialData, TableOne, TableTwo, TableThree, InitialData
from .serializers import InitialDataSerializer,\
    TableOneSerializer, TableTwoSerializer, TableThreeSerializer


class DataViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
    ):

    queryset = None
    serializer_class = None
    initial_fields = []

    def list(self, request, *args, **kwargs):
        initial_values = InitialData.objects.only(*self.initial_fields)
        initial_serializer = InitialDataSerializer(initial_values, many=True)
        table_data = self.get_queryset()
        table_serializer = self.get_serializer(table_data, many=True)
        combined_data = {
            'initial_data': initial_serializer.data,
            'table_data': table_serializer.data,
        }
        return Response(combined_data, status=status.HTTP_200_OK)


class InitialDataViewSet(DataViewSet):
    '''
    Класс предоставляет доступ к данным модели InitialData.
    Использует сериализатор InitialDataSerializer для сериализации данных.
    '''
    queryset = InitialData.objects.all()
    serializer_class = InitialDataSerializer


class TableOneViewSet(DataViewSet):
    '''
    Класс предоставляет доступ к данным модели TableOne, 
    а также возвращает соответствующие поля из модели InitialData.
    '''
    queryset = TableOne.objects.all()
    serializer_class = TableOneSerializer
    initial_fields = [
        'indicator_name',
        'unit',
        'plan_value',
    ]


class TableTwoViewSet(DataViewSet):
    '''
    Класс предоставляет доступ к данным модели TableTwo, 
    а также возвращает соответствующие поля из модели InitialData.
    '''
    queryset = TableTwo.objects.all()
    serializer_class = TableTwoSerializer
    initial_fields = [
        'event_name',
        'rf_set',
        'rb_set',
        'mb_set',
        'vnb_set',
    ]


class TableThreeViewSet(DataViewSet):
    '''
    Класс предоставляет доступ к данным модели TableThree, 
    а также возвращает соответствующие поля из модели InitialData.
    '''
    queryset = TableThree.objects.all()
    serializer_class = TableThreeSerializer
    initial_fields = [
        'event_name',
        'expected_result',
        'time_execution_plan',
    ]

