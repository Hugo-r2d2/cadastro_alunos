from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
        
# Cadastro de Professores
class Professor(models.Model): # Funcionando
    matricula_professor = models.AutoField(primary_key=True)
    nome_professor = models.CharField(max_length=200, null=True, blank=True)
    idade_professor = models.IntegerField(null=True, blank=True)
    ano_nascimento = models.DateField(null=True, blank=True)
    #materia_responsavel = models.ForeignKey(Materia, on_delete=models.PROTECT, default=1)

    def __str__(self):
        return self.nome_professor
    
    def clean(self):
        if not self.nome_professor:
            raise ValidationError("O nome do professor deve ser preenchido")

# Cadastro de Materias com Professores Responsáveis
class Materia(models.Model):
    nome = models.CharField(max_length=200, null=True, blank=True)
    professor_responsavel = models.ForeignKey(Professor, on_delete=models.PROTECT, default=1 )

    def __str__(self):
        return self.nome
    
    def clean(self):
        if not self.nome:
            raise ValidationError("O nome da matéria deve ser preenchido. ")
        
        #if not self.professor_responsavel:
        #    raise ValidationError("O professor responsável deve ser escolhido. ")

# Cadastro de Alunos
class Aluno(models.Model):
    matricula_aluno = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=200, null=True, blank=True)
    idade = models.IntegerField(null=True, blank=True)
    ano_nascimento = models.DateField(null=True, blank=True)
    materias_aluno = models.ManyToManyField(Materia)

    def __str__(self):
        return self.nome
    
    def clean(self):
        if not self.nome:
            raise ValidationError("O nome do aluno deve ser preenchido.")
        
class Nota(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    nota1 = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(10.0)], default=0)
    nota2 = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(10.0)], default=0)
    nota3 = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(10.0)], default=0)
    nota4 = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(10.0)], default=0)

    def calcular_media(self):
        return (self.nota1 + self.nota2 + self.nota3 + self.nota4) / 4.0

    def __str__(self):
        media = self.calcular_media()
        return f"Nota de {self.aluno.nome} em {self.materia.nome}: {self.nota1}, {self.nota2}, {self.nota3}, {self.nota4} - Média: {media:.2f}"

    class Meta:
        unique_together = ['aluno', 'materia']
