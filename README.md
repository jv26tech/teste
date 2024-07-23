# Python Web API

## Requisitos
- Python 3.10 ou superior
- PostgreSQL

## Instalação

1. Clone o repositório:
    ```bash
    git clone https://github.com/jv26tech/teste
    cd teste
    ```


2. Crie um ambiente virtual:
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

1. Execute o script para criar as tabelas:
    ```bash
    python main.py
    ```