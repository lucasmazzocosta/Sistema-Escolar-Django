from django import forms


# ERRO ENCONTRADO: o models está dentro da pasta portal, se passasse como estava o código dava erro, pois fora da pasta portal não tem um arquivo chamado models.py. 
# CORREÇÃO: Colocar a pasta portal no portal.models para o arquivo models seja encontrado.


from portal.models import Professor 

class ProfessorForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields = ['nome', 'sobrenome', 'email', 'telefone', 'registro',]
