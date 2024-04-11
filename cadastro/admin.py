from django.contrib import admin
from cadastro.models import Aluno, Professor, Materia

class AlunoAdmin(admin.ModelAdmin):
    list_display = (
        'nome',
        'idade',
        'ano_nascimento',
        )
    
    search_fields = (
        'matricula_aluno',
        'nome'
        )

class ProfessorAdmin(admin.ModelAdmin):
    list_display = (
        'nome_professor',
        'idade_professor',
        'ano_nascimento',
        'materia_responsavel'
        )
    
    search_fields = (
        'matricula_professor',
        'nome_professor',
        )
 
class MateriaAdmin(admin.ModelAdmin):
    list_display = (
        'nome',
        )
    
    search_fields = (
        'nome',
        )

admin.site.register(Aluno, AlunoAdmin)
admin.site.register(Professor, ProfessorAdmin)
admin.site.register(Materia, MateriaAdmin)
