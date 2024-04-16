- Este é um projeto para testar meus conhecimentos que utiliza Python e Django para cadastrar Matérias, Alunos e Professores.
- Para instalar em sua máquina siga os seguintes passos
  
  1° - Faça um git pull;
  2° - Crie um ambiente virtual no diretório do projeto:
        -> python3 -m venv venv
        -> source venv/bin/activate
  3° - Instale o Django:
        -> pip install django
  4° - Faça um migrate e um makemigrations:
        -> python3 manage.py migrate
        -> python3 manage.py makemigrations
  5° - Crie um usuário administrador
        -> python3 manage.py createsuperuser
  6° - Suba o projeto
        -> python3 manage.py runserver
