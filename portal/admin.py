from django.contrib import admin
from portal import models

@admin.register(models.Professor)
class ProfessorAdmin(admin.ModelAdmin):

    
# ERRO ENCONTRADO: Antes tinha o parâmetro 'especialidade', mas ele não existe na classe Professor. 
# CORREÇÃO: Se deve tirar ele, pois o que consta lá no models.py é disciplina, então se deve trocar para esse nome. 

    
    list_display = ('id', 'nome', 'email', 'disciplina', 'telefone', 'ativo',) 

@admin.register(models.Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email', 'telefone', 'ativo',)

@admin.register(models.Aula)
class AulaAdmin(admin.ModelAdmin):
    list_display = ('id', 'aluno_id', 'professor_id', 'status',)
