from django.urls import path
from app_1 import views

urlpatterns = [
    path('',views.listar_familia)
]
