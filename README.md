# Carrinho Seguidor de Linha (Django)

Este projeto é uma aplicação Django que simula e mostra o percurso de um
seguidor de linha. O carrinho possui dois motores conectados às rodas
dianteiras, uma roda de apoio na parte traseira e um sensor de linha preta. Os
motores e o sensor estão conectados a um Arduino Mega.

## Funcionalidades

- Simulação de dados de percurso do carrinho
- Armazenamento dos dados simulados no banco de dados
- Visualização do percurso do carrinho em um gráfico

## Pré-requisitos

- Python 3.6 ou superior
- Django 3.0 ou superior

## Instalação

Caso você não esteja usando Poetry, siga os passos abaixo para instalar e
executar o projeto:

1. Clone o repositório:

   ```bash
   git clone https://github.com/seu_usuario/seu_repositorio.git
   cd seu_repositorio
   ```

2. Crie e ative um ambiente virtual:

   ```bash
   python -m venv myenv
   source myenv/bin/activate  # No Windows, use: myenv\Scripts\activate
   ```

3. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

4. Configure o banco de dados e aplique as migrações:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. (Opcional) Crie um superusuário para acessar a interface de administração do Django:

   ```bash
   python manage.py createsuperuser
   ```

Caso você esteja usando Poetry, execute o comando abaixo para instalar as
dependências:

```bash
poetry install
```

## Simulação de Dados

Para simular e inserir dados de percurso no banco de dados, execute o comando de management `simulate_data`:

```bash
python manage.py simulate_data
```

## Executando o Servidor

Para iniciar o servidor de desenvolvimento do Django, execute:

```bash
python manage.py runserver
```

A aplicação estará disponível em http://127.0.0.1:8000/.

## Visualização do Gráfico

Acesse a rota http://127.0.0.1:8000/sensor/plot-data/ para visualizar o gráfico do percurso do carrinho.

## Estrutura do Projeto

```
myproject/
    ├── manage.py
    ├── myproject/
    │   ├── __init__.py
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    ├── sensor/
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── models.py
    │   ├── tests.py
    │   ├── views.py
    │   ├── urls.py
    │   ├── utils.py
    │   ├── migrations/
    │   │   └── __init__.py
    │   └── templates/
    │       └── sensor/
    │           └── plot.html
    ├── db.sqlite3
    ├── requirements.txt
    └── .gitignore
```
