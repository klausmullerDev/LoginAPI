
# LoginAPI

**LoginAPI** é uma aplicação web desenvolvida com **Python** e **Flask** para fornecer uma API RESTful para autenticação de usuários, utilizando **JSON Web Tokens (JWT)**. A aplicação também serve páginas HTML e CSS, além de usar JavaScript para a comunicação entre cliente e servidor.

## Tecnologias

- **Backend**: Python, Flask
- **Banco de Dados**: SQLite (ou qualquer outro banco configurado no `database.py`)
- **Autenticação**: Flask-JWT-Extended (JWT)
- **Frontend**: HTML, CSS, JavaScript
- **ORM**: SQLAlchemy (usado para interagir com o banco de dados)

## Requisitos

Antes de rodar o projeto, você precisará garantir que as seguintes dependências estão instaladas:

- **Python** 3.x ou superior
- **pip** (gerenciador de pacotes do Python)
- **Flask** (para o backend)
- **Flask-JWT-Extended** (para autenticação via JWT)
- **SQLAlchemy** (para interagir com o banco de dados)
- **HTML, CSS, JavaScript** (para o frontend)

## Instalação

1. **Clone o repositório**:

   No terminal, clone o repositório para o seu ambiente local:

   ```bash
   git clone https://github.com/klausmullerDev/LoginAPI.git
   cd LoginAPI
   ```

2. **Crie e ative um ambiente virtual**:

   Para evitar conflitos de versões de pacotes, é recomendado usar um ambiente virtual para o projeto.

   - No terminal, dentro da pasta do projeto, crie o ambiente virtual:

     ```bash
     python -m venv venv
     ```

   - Ative o ambiente virtual:

     - **Windows**:
       ```bash
       .\venv\Scripts\activate
       ```

     - **Mac/Linux**:
       ```bash
       source venv/bin/activate
       ```

3. **Instale as dependências**:

   Agora, instale as dependências do projeto (as bibliotecas que você usou no código, como Flask, Flask-JWT-Extended, etc.):

   ```bash
   pip install -r requirements.txt
   ```

   Se você não tiver o arquivo `requirements.txt`, você pode instalá-las manualmente:

   ```bash
   pip install flask flask-jwt-extended flask_sqlalchemy
   ```

4. **Configuração do banco de dados**:

   O projeto usa **SQLAlchemy** como ORM. Para criar as tabelas no banco de dados, execute o seguinte comando no terminal:

   ```bash
   python
   ```

   E dentro do shell interativo do Python:

   ```python
   from app import db
   db.create_all()
   ```

   Isso criará as tabelas definidas no seu modelo de banco de dados.

## Estrutura do Projeto

A estrutura do seu projeto pode ser algo assim:

```
LoginAPI/
│
├── app.py                # Arquivo principal do Flask, inicializa o servidor e a aplicação
├── config.py             # Arquivo de configurações da aplicação
├── database.py           # Configuração do banco de dados com SQLAlchemy
├── requirements.txt      # Arquivo com as dependências do projeto
├── auth.py               # Funções e rotas de autenticação
├── routes.py             # Rotas principais da API
├── templates/            # Arquivo de templates HTML
│   ├── index.html
│   ├── cadastro.html
│   └── bemvindo.html
└── static/               # Arquivos estáticos como CSS e JavaScript
    ├── style.css
    └── script.js
```

### Detalhes de cada arquivo:

- **`app.py`**: O arquivo principal onde a aplicação Flask é inicializada. Ele contém a configuração do app, as rotas principais e o banco de dados.
- **`config.py`**: Contém as configurações do aplicativo (por exemplo, chave secreta, configurações do banco de dados, etc.).
- **`database.py`**: Configurações do banco de dados com SQLAlchemy, incluindo a definição de modelos de dados, como o modelo `User`.
- **`auth.py`**: Contém as rotas e a lógica de autenticação de usuários.
- **`routes.py`**: Define as rotas principais da API.
- **`templates/`**: Contém os arquivos HTML usados para renderizar páginas no frontend.
- **`static/`**: Contém arquivos estáticos (CSS, JS) usados no frontend.

## Como Usar

1. **Rodar o servidor**:

   No terminal, com o ambiente virtual ativo, execute o servidor Flask:

   ```bash
   python app.py
   ```

   Isso iniciará a aplicação na URL padrão `http://127.0.0.1:5001`.

2. **Endpoints da API**:

   A API tem as seguintes rotas:

   - `POST /auth/login`: Para autenticar o usuário e retornar um token JWT.
   - `POST /auth/register`: Para cadastrar um novo usuário (com email e senha).
   - `GET /api/user`: Exemplo de rota protegida com JWT (requer um token JWT válido).

3. **Comunicação com a API**:

   Você pode fazer requisições para a API usando **JavaScript**. Aqui está um exemplo de como fazer uma requisição `POST` para login usando **fetch**:

   ```javascript
   fetch('http://127.0.0.1:5001/auth/login', {
     method: 'POST',
     headers: {
       'Content-Type': 'application/json'
     },
     body: JSON.stringify({
       username: 'seu_usuario',
       password: 'sua_senha'
     })
   })
   .then(response => response.json())
   .then(data => console.log(data));
   ```

4. **Frontend**:

   As páginas HTML do seu frontend estão localizadas na pasta `templates/` e os arquivos de estilo e scripts estão na pasta `static/`.


