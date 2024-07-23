import requests
from db import DB, Connection
from models import UserModel, PostModel
from views.post import PostView as PV
from views.user import UserView as UV
from config import Config

class Main:
    def __init__(self, conn: Connection) -> None:
        self.db = DB(conn)
        
    def task(self):
        conn = self.db.conn
        tabelas = [UserModel, PostModel]
        self.db.criar_tabelas(tabelas)
        self.db.limpar_tabelas()

        pv = PV()
        uv = UV()


        posts = pv.listar()
        for post in posts[:5]:
            post = PostModel(post['userId'], post['title'], post['body'])
            post_id = self.db.create(post)
            print(f"Post inserido com ID: {post_id}")

        novo_post = pv.criar('Título de Teste', 'Corpo de Teste', 1)
        if novo_post:
            post = PostModel(novo_post['userId'], novo_post['title'], novo_post['body'])
            post_id = self.db.create(post)
            print(f"Novo post inserido com ID: {post_id}")

            atual_post = pv.modificar(1, "Titulo Atualizado", "Corpo Atualizado", 2)
            print(f"Post de id {post_id} modificado.")

            post = PostModel(atual_post['userId'], atual_post['title'], atual_post['body'])
            self.db.update(post, post_id)
            print(f"Post de id {post_id} atualizado no banco.")

            post = pv.remover(post_id)
            print(f"Post removido {post}")
            post_id = self.db.delete(PostModel, post_id)
            print(f"Post removido do banco com ID: {post_id}")

        users = uv.listar()
        for user in users:
            usr = UserModel(**user)
            post_id = self.db.create(usr)
            print(f"User { user['username'] } inserido com ID: {post_id}")

        self.db.desconectar()

    

if __name__ == '__main__':
    conn = Connection(Config)
    Main(conn).task()
