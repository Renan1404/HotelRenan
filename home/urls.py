from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', home , name="home"),
    path('acomodacoes/', acomodacoes, name="acomodacoes"),  
    path('refeicoes/', refeicoes, name="refeicoes"),  
    path('depoimentos/', depoimentos, name="depoimentos"),  
    path('bebidas/', bebidas, name="bebidas"),  
    path('lazer/', lazer, name="lazer"),  
]