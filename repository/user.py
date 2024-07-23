
class UserDB:
    """
        CRUD para interagir com a tabela 'users'
    """
    def db_create(conn, name, username, email, phone, website):
        with conn.cursor() as cursor:
            cursor.execute("""
            INSERT INTO users (name, username, email, phone, website) VALUES (%s, %s, %s, %s, %s) RETURNING id;
            """, (name, username, email, phone, website))
            user_id = cursor.fetchone()[0]
            conn.commit()
        return user_id

    def db_get(conn, id):
        with conn.cursor() as cursor:
            cursor.execute("SELECT FROM users WHERE id=%s;", (id,))
            users = cursor.fetchall()
        return users

    def db_get_all(conn):
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM users;")
            users = cursor.fetchall()
        return users


    def db_update(conn, user_id, name, username, email, phone, website):
        with conn.cursor() as cursor:
            cursor.execute("""
            UPDATE users SET name=%s, username=%s, email=%s, phone=%s, website=%s WHERE id=%s;
            """, (name, username, email, phone, website, user_id))
            conn.commit()
            return user_id



    def db_delete(conn, user_id):
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM users WHERE id=%s;", (user_id,))
            conn.commit()
            return user_id
