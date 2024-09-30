from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets, mixins

from .models import InitialData, TableOne, TableTwo, TableThree, InitialData
from .serializers import InitialDataSerializer,\
    TableOneSerializer, TableTwoSerializer, TableThreeSerializer

from typing import Type, List
from django.db.models import Model
from django.core.serializers import Serializer

class InitialDataViewSet(viewsets.ModelViewSet):
    queryset = InitialData.objects.all()
    serializer_class = InitialDataSerializer

class TableOneViewSet(viewsets.ModelViewSet):
    queryset = TableOne.objects.all()
    serializer_class = TableOneSerializer

class TableTwoViewSet(viewsets.ModelViewSet):
    queryset = TableTwo.objects.all()
    serializer_class = TableTwoSerializer

class TableThreeViewSet(viewsets.GenericViewSet):
    queryset = TableThree.objects.all()
    serializer_class = TableThreeSerializer

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
        

class DataAPIView(APIView):
    '''
    Универсальный APIView для таблиц
    
    - model: Ссылка на модель
    - serializer_class: Сериализатор для модели
    - initial_fields: Поля из InitialData, которые включены в ответ на GET запрос.
    '''

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
        table_serializer = self.get_serializer(table_data, many=True)

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
    
    def put(self, request, pk):
        '''
        Метод обновляет существующий объект в базе данных.

        - pk: первичный ключ объекта, который необходимо обновить.

        return: объект Response с данными о обновленном объекте или ошибками валидации:
            - статус 200 (OK) успешная валидация.
            - статус 400 (BAD REQUEST) ошибка валидации.
            - статус 404 (NOT FOUND) если объект не найден.
        '''
        try:
            instance = self.model.objects.get(pk=pk)
        except self.model.DoesNotExist:
            return Response({'error': 'Object not found.'}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        '''
        Метод удаляет существующий объект из базы данных.

        - pk: первичный ключ объекта, который необходимо удалить.

        return: объект Response с статусом удаления:
            - статус 204 (NO CONTENT) успешное удаление.
            - статус 404 (NOT FOUND) если объект не найден.
        '''
        try:
            instance = self.model.objects.get(pk=pk)
            instance.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except self.model.DoesNotExist:
            return Response({'error': 'Object not found.'}, status=status.HTTP_404_NOT_FOUND)


class InitialDataView(DataViewSet):
    '''
    Класс предоставляет доступ к данным модели InitialData.
    Использует сериализатор InitialDataSerializer для сериализации данных.
    '''
    queryset = InitialData.objects.all()
    serializer_class = InitialDataSerializer


class TableOneAPIView(DataViewSet):
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


class TableTwoAPIView(DataViewSet):
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


class TableThreeAPIView(DataViewSet):
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

