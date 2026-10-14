# Sistema Escolar Django — Atividade Ciclo 1 (Estrutura de Dados)

**Alunos:** Lucas Mazzo e Dimitri

## Descrição do projeto

O prjeto consiste em um sistema escolar feito em Django para gerenciar **Professores**, **Alunos** e **Aulas**.
O projeto base foi entregue com 8 erros propositais. Nesta atividade os 8 erros foram
encontrados, corrigidos e comentados diretamente no código, no formato `# ERRO ENCONTRADO:` e `#CORREÇÃO:`.

O código fica em `sistema_escolar_django-main`:

- `sistema/` — configurações do projeto (settings e URLs globais)
- `portal/` — app com models, views, forms, admin, URLs e templates

## Os 8 erros encontrados

01 | `portal/models.py` | `timezone.now` era usado em `criacao_data` e `horario`, mas o `timezone` não era importado. Foi adicionado `from django.utils import timezone` (o do Django, não o `datetime.timezone` do Python, que não tem `.now`).
02 | `portal/models.py` | O campos `matricula` precisava ser unico, então foi colocado `(unique=True)` para que não haja duplicação de matrícula.
03 | `portal/views.py` | O template era chamado como `'templates/portal/index.html'`. Como o Django já procura dentro de `templates/`, o caminho ficava duplicado. O caminho foi trocado para `'portal/index.html'`.
04 | `portal/forms.py` | `from models import Professor` procura um módulo `models` na raiz do projeto, que não existe. Foi trocado para `from portal.models import Professor`.
05 | `portal/admin.py` | O `list_display` do `ProfessorAdmin` usava `'especialidade'`, campo que não existe no models.py. Foi substituído pelo campo real `'disciplina'`.
06 | `portal/urls.py` | A rota `cadastro/` apontava para `views.cadastro`, função que não existe. Com isso, foi removida a rota que apontava para uma view inexistente.
07 | `sistema/urls.py` | Havia um texto solto no lugar da view e as URLs do app `portal` nunca eram ligadas ao projeto. Foi importado o `include` e adicionado `path('', include('portal.urls'))`.
08 | `sistema/settings.py` | O app `portal` não estava no `INSTALLED_APPS`, então o Django não reconhecia models, templates nem o admin do app. | Foi adicionado `'portal'` ao `INSTALLED_APPS`.

## Como rodar o projeto localmente

```bash
# Clonar o repositório
git clone https://github.com/lucasmazzocosta/Ciclo-1-Estrutura-de-Dados.git
cd Ciclo-1-Estrutura-de-Dados/sistema_escolar_django-main

# Instalar o Django
pip manage.py django

# Criar as tabelas do banco
python manage.py makemigrations
python manage.py migrate

# (Opcional) Criar um usuário para o admin
python manage.py createsuperuser

# 6. Rodar o servidor
python manage.py runserver
```

Depois acesse:

- http://127.0.0.1:8000/admin/ — painel administrativo (Professores, Alunos e Aulas)
