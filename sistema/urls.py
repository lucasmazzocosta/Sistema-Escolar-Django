from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    
    # ERRO ENCONTRADO: no lugar da view tinha um texto solto, que ocasionava um erro, com isso as rotas do app Portal nunca eram ligadas ao projeto. 
    # CORREÇÃO: A correção foi incluir essas rotas do app Portal e importar o include para que desse certo essa inclusão.
    
    
    path('', include('portal.urls')), 
]
