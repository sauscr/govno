from rest_framework import viewsets
from reports.models import InitialData, TableOne, TableTwo, TableThree
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
