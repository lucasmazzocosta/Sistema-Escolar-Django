from django.urls import path

from portal import views

urlpatterns = [
    path('index/', views.index), # ERRO ENCONTRADO: Antes tinha uma path de cadastro, mas ela não existe no views.py, só existe apenas o index, ou seja, dava erro pois não existia a path cadastro. CORREÇÃO: A path de cadastro deve ser retirada do urlpatterns.
]
