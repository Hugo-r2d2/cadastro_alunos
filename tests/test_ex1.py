import pytest
from cadastro.models import Materia, Professor, Aluno

@pytest.mark.django_db
def test_materia_creation():
    materia = Materia.objects.create(nome="Matemática")
    assert materia.nome == "Matemática"

@pytest.mark.django_db
def test_professor_creation():
    # Criar uma matéria para associar ao professor
    materia = Materia.objects.create(nome="Matemática")
    
    # Criar o professor associado à matéria
    professor = Professor.objects.create(nome_professor="Joao", idade_professor=20, materia_responsavel=materia)
    
    assert professor.nome_professor == "Joao"
    assert professor.idade_professor == 20


@pytest.mark.django_db
def test_aluno_creation():
    aluno = Aluno.objects.create(nome="Maria", idade=25, ano_nascimento="1999-01-01")
    assert aluno.nome == "Maria"
    assert aluno.idade == 25
