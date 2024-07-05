# Projeto de Cadastro de Matérias, Alunos e Professores

Este é um projeto desenvolvido com Python e Django que permite o cadastro e gerenciamento de Matérias, Alunos e Professores.

## Pré-requisitos

Certifique-se de ter o Python 3 instalado em sua máquina.

## Instalação

Siga os passos abaixo para configurar e executar o projeto em sua máquina local:

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/HugoSantos2131/cadastro_alunos.git
   cd cadastro_alunos
   ```

2. **Crie um ambiente virtual no diretório do projeto:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Para Windows, use `venv\Scripts\activate`
   ```

3. **Instale as dependências:**

   ```bash
   pip install django
   ```

4. **Configure o banco de dados:**

   ```bash
   python3 manage.py migrate
   python3 manage.py makemigrations
   python3 manage.py migrate
   ```

5. **Crie um superusuário:**

   ```bash
   python3 manage.py createsuperuser
   ```

6. **Inicie o servidor de desenvolvimento:**

   ```bash
   python3 manage.py runserver
   ```

## Uso

Após iniciar o servidor, acesse `http://127.0.0.1:8000/` em seu navegador para utilizar o sistema. Para acessar a área administrativa, vá para `http://127.0.0.1:8000/admin/` e entre com as credenciais do superusuário que você criou.

## Contribuição

Se você quiser contribuir com este projeto, siga os passos abaixo:

1. Faça um fork do projeto.
2. Crie uma nova branch: `git checkout -b minha-nova-feature`
3. Faça suas modificações e commit: `git commit -m 'Adiciona minha nova feature'`
4. Envie para a branch principal: `git push origin minha-nova-feature`
5. Abra um Pull Request.
