# reports/urls.py
from django.urls import path, include
from .views import (
    InitialDataViewSet,
    TableOneViewSet,
    TableTwoViewSet,
    TableThreeViewSet,
    )

from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register(r'initialdata', InitialDataViewSet)
router.register(r'tableone', TableOneViewSet)
router.register(r'tabletwo', TableTwoViewSet)
router.register(r'tablethree', TableThreeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]