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
    '''Универсальный APIView для таблиц'''

    model = None
    serializer_class = None
    initial_fields = []

    
    def get(self, request):
        '''
        Метод извлекает данные из модели и возвращает их в формате JSON.

        - self.initial_fields: список полей, которые будут извлечены из модели `InitialData`.
        - self.table_fields: список полей, которые будут извлечены из модели,
        заданной в `self.model`.
        
        return: объект Response с данными в формате JSON, содержащий:
            - initial_data: данные из модели `InitialData`,
            сериализованные с использованием `InitialDataSerializer`.
            - table_data: данные из модели, заданной в `self.model`,
            сериализованные с использованием `self.serializer_class`.
        '''
        values = InitialData.objects.only(*self.initial_fields)
        initial_serializer = InitialDataSerializer(values, many=True)

        table_data = self.model.objects.all()
        table_serializer = self.serializer_class(table_data, many=True)

        combined_data = {
            'initial_data': initial_serializer.data,
            'table_data': table_serializer.data,
        }
        return Response(combined_data, status=status.HTTP_200_OK)
    

    def post(self, request):
        '''
        Метод принимает данные от клиента, валидирует их и сохраняет в базе данных.

        - self.serializer_class: сериализатор,
        используемый для валидации и сохранения данных.

        return: объект Response с данными о созданном объекте или ошибками валидации:
            - статус 201 (CREATED) успешная валидация.
            - статус 400 (BAD REQUEST) ошибка валидации.
        '''
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class InitialDataView(DataAPIView):
    '''API для InitialData'''
    model = InitialData
    serializer_class = InitialDataSerializer


class TableOneAPIView(DataAPIView):

    model = TableOne
    serializer_class = TableOneSerializer
    initial_fields = [
        'indicator_name',
        'unit',
        'plan_value',
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


class TableThreeAPIView(DataAPIView):

    model = TableThree
    serializer_class = InitialDataSerializer
    initial_fields = [
        'event_name',
        'expected_result',
        'time_execution_plan',
    ]
