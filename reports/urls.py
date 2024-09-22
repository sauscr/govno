# reports/urls.py
from django.urls import path, include
from .views import InitialDataView,\
    TableOneAPIView, TableTwoAPIView, TableThreeAPIView,\
    InitialDataViewSet, TableOneViewSet, TableTwoViewSet, TableThreeViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register(r'initialdata', InitialDataViewSet)
router.register(r'tableone', TableOneViewSet)
router.register(r'tabletwo', TableTwoViewSet)
router.register(r'tablethree', TableThreeViewSet)

urlpatterns = [
    path('data/', InitialDataView.as_view(), name = 'data_view'),
    path('one/', TableOneAPIView.as_view(), name = 'indicator_one'),
    path('two/', TableTwoAPIView.as_view(), name = 'indicator_two'),
    path('three/', TableThreeAPIView.as_view(), name='indicator_three'),
    path('', include(router.urls)),
]

