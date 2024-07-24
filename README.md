# Python Web API

## Requisitos (execucao por venv)
- Python 3.10 ou superior
- PostgreSQL

## Requisitos (execucao por Docker)
- Docker
- docker-compose

## Instalação

1. Clone o repositório:
    ```bash
    git clone https://github.com/jv26tech/teste
    cd teste
    ```

2. Crie um ambiente virtual (ou siga para execucao com docker):
    ```bash
    python -m venv venv
    ```

3. Execute o ambiente virtual (*Linux*):
    ```bash
    source venv/bin/activate
    ```

3. Execute o ambiente virtual (*Windows*):
     ```bash
    ./venv/Scripts/activate.bat
    ```

4. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

5. Configure o banco de dados PostgreSQL:
    - Crie um banco de dados e atualize as informações de conexão no arquivo `.env`.


## Execução

1. (Docker) Execute o comando para subir os conteineres (app, postgres e pgadmin)
    ```bash
    docker-compose up
    ```

1. (venv) Execute o script para criar as tabelas e rodar comandos CRUD:
    ```bash
    python main.py
    ```


## Autor
Joao Victor Ferrer Morgado