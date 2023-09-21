# API de Gerenciamento de Disciplinas e Tarefas de Alunos

Esta é uma API construída em Django para ajudar alunos a gerenciarem suas disciplinas e tarefas de forma eficiente. A API permite que você crie, liste, atualize e exclua alunos, disciplinas e tarefas associadas a cada aluno.


## Iniciando a API

Siga os passos abaixo para iniciar a API:

1. Clone o repositório:

   ```bash
   git clone https://github.com/RafaMattss/apiAula.git

2. Crie um ambiente virtual (recomendado) e ative-o:

    bash
    Copy code
    python -m venv .env
    python .\.env\Scripts\activate

3. Instale as dependências:
    pip install -r requirements.txt

4. Execute as migrações do banco de dados:
    python manage.py makemigrations
    python manage.py migrate

5. Inicie o servidor de desenvolvimento:
    python manage.py runserver


A API estará disponível em http://localhost:8000/.

Uso da API
A API oferece as seguintes endpoints:

/api/students/: Gerencie alunos (CRUD).
/api/disciplines/: Gerencie disciplinas (CRUD).
/api/tasks/: Gerencie tarefas (CRUD).
/api/students/<students_id>/tasks/: Liste as tarefas de um aluno específico.
Você pode usar ferramentas como o Postman ou fazer solicitações HTTP diretas para interagir com a API.

Exemplos de Solicitações
Aqui estão alguns exemplos de solicitações:

Criar um Aluno: Envie uma solicitação POST para /api/students/ com dados JSON.
Listar Tarefas de um Aluno: Envie uma solicitação GET para /api/students/<students_id>/tasks/.
Atualizar uma Disciplina: Envie uma solicitação PUT para /api/disciplines/<disciplines_id>/ com dados JSON.
Excluir uma Tarefa: Envie uma solicitação DELETE para /api/tasks/<tasks_id>/.
Certifique-se de incluir os cabeçalhos apropriados e dados JSON conforme necessário.

Lembre-se de que esta é uma API de exemplo e pode ser estendida e personalizada de acordo com suas necessidades.



Exemplos de modelos JSON para poder testar nos endpoints:
    Disciplinas:
        {
            "name": "Lógica de Programação",
            "description": "Aprende Lógica de Programação"
        }

    Alunos:
        {
            "name": "rafao",
            "email": "rafael@gmail.com"
        }   

    Tarefas: 
        {
            "title": "Tarefa 1",
            "description": "Descrição da Tarefa 1",
            "issue_date": "2023-09-23",
            "completed": false,
            "students": 1,
            "disciplines": [1]
        }

    
Todos os métodos POST retornarão em Json o objeto criado e o status HTTP_201_CREATED ,
Todos os métodos GET retornarão em Json o objeto chamado,
Todos os métodos PUT retornarão em Json o objeto modificado e o status HTTP_201_CREATED,
Todos os métodos DELETE retornarão o status HTTP_204_NO_CONTENT.