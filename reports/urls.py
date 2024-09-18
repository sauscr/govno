# reports/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('data/', views.data_view, name = 'data_view'),
    path('one/', views.view_table_one, name = 'indicator_one'),
    path('two/', views.view_table_two, name = 'indicator_two'),
    path('three/', views.view_table_three, name='indicator_three'),
]

