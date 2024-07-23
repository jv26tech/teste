import psycopg2
from config import Config
from models import BaseModel

class Connection: 
    def __init__(self, config:Config):
        self.DB = config.DATABASE
            
    
    def conectar_bd(self):
        """
            Cria e retorna a conexao para o banco de dados.
        """
        self.conn = psycopg2.connect(**self.DB)
        return self.conn
    

class DBBase:
    tables:list[BaseModel] = []

    def __init__(self, conexao:Connection) -> None:
        self.conn = conexao.conectar_bd()


    def create(self, model:BaseModel):
        """
            Cria um registro no banco de dados e retorna seu id.
        """
        with self.conn.cursor() as cursor:
            keys = [col for col in model.get_data().keys()]
            keysstr = ', '.join(keys)
            values = tuple(model.data[key] for key in keys)
            query = f"INSERT INTO { model.tablename } ({ keysstr }) \
                VALUES ({', '.join([r"%s" for v in values])}) RETURNING id;"
            cursor.execute(query, values)
            id = cursor.fetchone()[0]
            self.conn.commit()
            return id

    def read(self, model:BaseModel, id):
        """
            Le um registro no banco de dados e o retorna.
        """
        with self.conn.cursor() as cursor:
            query = f"SELECT FROM { model.tablename } WHERE id=%s;"
            cursor.execute(query, (id,))
            res = cursor.fetchone()[0]
            self.conn.commit()
            return res

    def read_all(self, model:BaseModel):
        """
            Le todos os registros no banco de dados e os retorna.
        """
        with self.conn.cursor() as cursor:
            query = f"SELECT * FROM {model.tablename};"
            cursor.execute(query)
            res = cursor.fetchall()
            self.conn.commit()
            return res

    def update(self, model:BaseModel, id):
        """
            Atualiza um registro no banco de dados e retorna seu id.
        """
        with self.conn.cursor() as cursor:
            keys = [col for col in model.get_data().keys()]
            keysstr = ', '.join(keys)
            values = tuple(model.data[key] for key in keys)
            query = f"UPDATE {model.tablename} SET {', '.join([f"{key}=%s" for key in keys])} WHERE id={id};"
            cursor.execute(query, values)
            self.conn.commit()
            return id

    def delete(self, model:BaseModel, id):
        """
            Remove um registro no banco de dados e retorna seu id.
        """
        with self.conn.cursor() as cursor:
            cursor.execute(f"DELETE FROM {model.tablename} WHERE id=%s;", (id,))
            self.conn.commit()
            return id


class DB(DBBase):

    def criar_tabelas(self, tables:list[BaseModel]) -> None:
        """
            Cria as tabelas no banco a partir de uma lista de modelos.
        """
        with self.conn.cursor() as cursor:
            for tab in tables:
                cursor.execute(tab.table)
            self.conn.commit()
            self.tables = tables


    def limpar_tabelas(self) -> None:
        """
            Limpa as tabelas do banco de dados.
        """
        with self.conn.cursor() as cursor:
            if len(self.tables) > 0:
                for tab in self.tables:
                    cursor.execute(f"DELETE FROM {tab.tablename};")
                    cursor.execute(f"ALTER SEQUENCE {tab.tablename}_id_seq RESTART WITH 1")
                self.conn.commit()
                print('TABELAS LIMPAS E RESETADAS')
            else:
                print('NENHUMA TABELA ENCONTRADA')

    def desconectar(self) -> None:
        """
            Desconecta do banco de dados.
        """
        self.conn.close()
