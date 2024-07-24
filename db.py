import psycopg2
from config import Config
from models import BaseModel
import time

class Connection:
    def __init__(self, config: Config):
        self.db_config = config.DATABASE
        self.conn = None

    def connect(self) -> psycopg2.extensions.connection:
        """Cria e retorna a conexão para o banco de dados."""
        if self.conn is None or self.conn.closed:
            try:
                self.conn = psycopg2.connect(**self.db_config)
            except psycopg2.OperationalError:
                time.sleep(3)
                self.conn = psycopg2.connect(**self.db_config)
        return self.conn

    def disconnect(self) -> None:
        """Desconecta do banco de dados."""
        if self.conn and not self.conn.closed:
            self.conn.close()

class QueryExecutor:
    def __init__(self, connection: Connection):
        self.connection = connection.connect()

    def execute_query(self, query: str, params: tuple = ()) -> list:
        with self.connection.cursor() as cursor:
            cursor.execute(query, params)
            query_upper = query.strip().upper()
            if query_upper.startswith("SELECT"):
                result = cursor.fetchall()
            elif query_upper.startswith("SELECT") or query_upper.startswith("UPDATE") or query_upper.startswith("INSERT"):
                result = cursor.fetchone()
            else:
                result = [{}]
            self.connection.commit()
        return result

class DBBase:
    def __init__(self, query_executor: QueryExecutor):
        self.query_executor = query_executor

    def create(self, model: BaseModel) -> int:
        """Cria um registro no banco de dados e retorna seu id."""
        keys = ', '.join(model.data.keys())
        values = tuple(model.data[key] for key in model.data.keys())
        placeholders = ', '.join(['%s'] * len(values))
        query = f"INSERT INTO {model.tablename} ({keys}) VALUES ({placeholders}) RETURNING id;"
        result = self.query_executor.execute_query(query, values)
        return result[0]

    def read(self, model: BaseModel, record_id: int) -> tuple:
        """Lê um registro no banco de dados e o retorna."""
        query = f"SELECT * FROM {model.tablename} WHERE id = %s;"
        result = self.query_executor.execute_query(query, (record_id,))
        return result[0]

    def read_all(self, model: BaseModel) -> list:
        """Lê todos os registros no banco de dados e os retorna."""
        query = f"SELECT * FROM {model.tablename};"
        result = self.query_executor.execute_query(query)
        return result

    def update(self, model: BaseModel, record_id: int) -> int:
        """Atualiza um registro no banco de dados e retorna seu id."""
        keys_values = ', '.join([f"{key} = %s" for key in model.data.keys()])
        values = tuple(model.data[key] for key in model.data.keys())
        query = f"UPDATE {model.tablename} SET {keys_values} WHERE id = %s RETURNING id;"
        result = self.query_executor.execute_query(query, values + (record_id,))
        return result[0]

    def delete(self, model: BaseModel, record_id: int) -> int:
        """Remove um registro no banco de dados e retorna seu id."""
        query = f"DELETE FROM {model.tablename} WHERE id = %s RETURNING id;"
        result = self.query_executor.execute_query(query, (record_id,))
        return result[0]

class DBManager(DBBase):
    def __init__(self, query_executor: QueryExecutor):
        super().__init__(query_executor)

    def create_tables(self, tables: list[BaseModel] = []) -> None:
        """Cria as tabelas no banco a partir de uma lista de modelos."""
        self.tables = tables
        for table in self.tables:
            self.query_executor.execute_query(table.table)

    def clear_tables(self) -> None:
        """Limpa as tabelas do banco de dados."""
        for table in self.tables:
            self.query_executor.execute_query(f"DELETE FROM {table.tablename};")
            print('Deletado')
            self.query_executor.execute_query(f"ALTER SEQUENCE {table.tablename}_id_seq RESTART WITH 1;")
        print("TABELAS LIMPAS E RESETADAS")
