from django.contrib import admin
from cadastro.models import Aluno, Professor, Materia, Nota

class NotaInline(admin.TabularInline):
    model = Nota
    extra = 1

class AlunoAdmin(admin.ModelAdmin):
    inlines = [NotaInline]

    list_display = (
        'nome',
        'idade',
        'ano_nascimento',
        'display_professores_materias',  # Método personalizado para exibir as matérias e professores
    )
    
    search_fields = (
        'matricula_aluno',
        'nome'
    )
    
    def display_professores_materias(self, obj):
        materias_professores = []
        for materia in obj.materias_aluno.all():
            materias_professores.append(f"// {materia.nome} - {materia.professor_responsavel.nome_professor} // ")
        return " ".join(materias_professores) 
    
    display_professores_materias.short_description = 'Matérias e Professores'  # Define o título da coluna

class ProfessorAdmin(admin.ModelAdmin):
    list_display = (
        'nome_professor',
        'idade_professor',
        'ano_nascimento',
    )
    
    search_fields = (
        'matricula_professor',
        'nome_professor',
    )
 
class MateriaAdmin(admin.ModelAdmin):
    inlines = [NotaInline]

    list_display = (
        'nome',
        'professor_responsavel',
    )
    
    search_fields = (
        'nome',
    )

class NotaAdmin(admin.ModelAdmin):
    list_display = (
        'aluno',
        'materia',
        'nota1',
        'nota2',
        'nota3',
        'nota4',
    )

    search_fields = (
        'aluno__nome',
        'materia__nome',
    )


admin.site.register(Aluno, AlunoAdmin)
admin.site.register(Professor, ProfessorAdmin)
admin.site.register(Materia, MateriaAdmin)
admin.site.register(Nota, NotaAdmin)
