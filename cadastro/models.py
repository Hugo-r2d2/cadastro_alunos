from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator

# Cadastro de Materias com Professores Responsáveis
class Materia(models.Model):
    nome = models.CharField(max_length=200, null=True, blank=True)
    #professor_responsavel = models.ForeignKey(Professor, on_delete=models.PROTECT )

    def __str__(self):
        return self.nome
    
    def clean(self):
        if not self.nome:
            raise ValidationError("O nome da matéria deve ser preenchido. ")
        
        #if not self.professor_responsavel:
        #    raise ValidationError("O professor responsável deve ser escolhido. ")
        
# Cadastro de Professores
class Professor(models.Model): # Funcionando
    matricula_professor = models.AutoField(primary_key=True)
    nome_professor = models.CharField(max_length=200, null=True, blank=True)
    idade_professor = models.IntegerField(null=True, blank=True)
    ano_nascimento = models.DateField(null=True, blank=True)
    materia_responsavel = models.ForeignKey(Materia, on_delete=models.PROTECT, default=1)

    def __str__(self):
        return self.nome_professor
    
    def clean(self):
        if not self.nome_professor:
            raise ValidationError("O nome do professor deve ser preenchido")

# Cadastro de Alunos
class Aluno(models.Model):
    matricula_aluno = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=200, null=True, blank=True)
    idade = models.IntegerField(null=True, blank=True)
    ano_nascimento = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.nome
    
    def clean(self):
        if not self.nome:
            raise ValidationError("O nome do aluno deve ser preenchido.")
        