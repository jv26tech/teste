from db import DB


class PostDB:
    """
        CRUD para interagir com a tabela 'posts'
    """
    def __init__(self, db:DB) -> None:
        self.db

    def db_create(conn, user_id, title, body):
        with conn.cursor() as cursor:
            cursor.execute("""
            INSERT INTO posts (user_id, title, body) VALUES (%s, %s, %s) RETURNING id;
            """, (user_id, title, body))
            post_id = cursor.fetchone()[0]
            conn.commit()
            return post_id
        
    def db_get(conn, id):
        with conn.cursor() as cursor:
            cursor.execute("""
            SELECT FROM posts WHERE id=%s;
            """, (id,))
            post = cursor.fetchone()[0]
            conn.commit()
            return post

    def db_get_all(conn):
        with conn.cursor() as cursor:
            cursor.execute("""
            SELECT * FROM posts;
                        """)
            posts = cursor.fetchall()
            conn.commit()
            return posts

    def db_update(conn, id, user_id, title, body):
        with conn.cursor() as cursor:
            cursor.execute("""
            UPDATE posts SET title=%s, body=%s, user_id=%s WHERE id=%s;
            """, (title, body, user_id, id))
            conn.commit()
            return id
        

    def db_delete(conn, id):
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM posts WHERE id=%s;", (id,))
            conn.commit()
            return id
        

