from dotenv import load_dotenv
import os

load_dotenv()

class BaseConfig:
    BASE_URL:str
    DATABASE:str


class Config(BaseConfig):
    BASE_URL = 'https://jsonplaceholder.typicode.com'

    DATABASE = {
        'dbname': os.getenv('DB_NAME'),
        'user': os.getenv('DB_USER'),
        'password': os.getenv('DB_PASS'),
        'host': os.getenv('DB_HOST'),
        'port': os.getenv('DB_PORT')
    }

class TestConfig(BaseConfig):
    pass