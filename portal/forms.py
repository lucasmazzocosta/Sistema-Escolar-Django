from django import forms

from portal.models import Professor # ERRO ENCONTRADO: o models está dentro da pasta portal, se pasasse como estava o código dava erro, pois fora da pasta portal não tem um arquivo chamado models.py. CORREÇÃO: Colocar a pasta portal no portal.models para o arquivo models seja encontrado.

class ProfessorForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields = ['nome', 'sobrenome', 'email', 'telefone', 'registro',]
