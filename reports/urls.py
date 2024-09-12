# reports/urls.py
from django.urls import path
from . import views

urlpatterns = [

    path('', views.target_indicator_view, name = 'target_indicator'),


]

