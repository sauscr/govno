from config.urls import path
from ..reports import views

urlpatterns = [
    path('fastapi/', views.call_fastapi),
]