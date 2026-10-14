from django.shortcuts import render


def index(request):
    return render(
        request,
        'portal/index.html' # ERRO ENCONTRADO: Por causa do APP_DIRS o Django já procura dentro da pasta template, ou seja ele buscava um arquivo que não existe iria ficar templates/templates/portal/index.html. CORREÇÃO: A correção feita foi tirar o templates para o django já buscar a partir dessa pasta.
    )
