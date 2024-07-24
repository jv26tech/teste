import requests
from db import Connection, QueryExecutor, DBManager, DBBase

from models import UserModel, PostModel

from config import Config
from scripts import *

class Main:
    def __init__(self, db:DBBase) -> None:
        self.db = db

    def setup(self):
        tables = [
            UserModel, PostModel
        ]
        ScriptSetupDB(manager, tables)
        
    def run(self):
        self.setup()
        ScriptFillTables(self.db)
        ScriptPost(self.db)
        ScriptUser(self.db)
        

    

if __name__ == '__main__':
    conn = Connection(Config)
    qe = QueryExecutor(conn)
    manager = DBManager(qe)
    main = Main(manager)
    main.run()
    conn.disconnect()
