# reports/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('target-indicators/', views.target_indicator_list, name='target_indicator_list'),
    path('target-indicators/new/', views.target_indicator_new, name='target_indicator_new'),
    path('target-indicators/<int:pk>/', views.target_indicator_detail, name='target_indicator_detail'),
    path('target-indicators/<int:pk>/edit', views.target_indicator_edit, name='target_indicator_edit'),
    path('activities/', views.activity_list, name='activity_list'),
    path('activities/new', views.activity_new, name='activity_new'),
    path('activities/<int:pk>', views.activity_detail, name='activity_detail'),
    path('activities/<int:pk>/edit', views.activity_edit, name='activity_edit'),
    # path('somePath/', views.somePath_list, name='somePath_list'),
    # path('somePath/new', views.somePath_new, name='somePath_new'),
    # path('somePath/<int:pk>', views.somePath_detail, name='somePath_detail'),
    # path('somePath/<int:pk>/edit', views.somePath_edit, name='somePath_edit'),
    # path('somePath/', views.somePath_list, name='somePath_list'),
    # path('somePath/new', views.somePath_new, name='somePath_new'),
    # path('somePath/<int:pk>', views.somePath_detail, name='somePath_detail'),
    # path('somePath/<int:pk>/edit', views.somePath_edit, name='somePath_edit'),
        # Add paths for other models
]
