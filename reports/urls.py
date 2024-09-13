from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_table_one, name='indicator_one'),  # one/
    path(' /edit/<int:id>/', views.edit_tableone, name='edit_indicator_one'),  # Редактирование
    path(' /delete/<int:id>/', views.delete_tableone, name='delete_indicator_one'),  # Удаление
    path('two/', views.view_table_two, name='indicator_two'),
]
