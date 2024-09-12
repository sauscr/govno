# reports/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('one/', views.view_table_one, name = 'indicator_one'),
    path('two/', views.view_table_two, name = 'indicator_two'),
]

