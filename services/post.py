import requests
from config import Config


class PostService:
    """
        CRUD para interagir com o endpoint '/posts'
    """
    
    def __init__(self, config:Config):
        self.BASE_URL = config.BASE_URL  

    def criar(self, titulo, corpo, user_id) -> dict:
        payload = {
            'title': titulo,
            'body': corpo,
            'userId': user_id
        }
        response = requests.post(f'{self.BASE_URL}/posts', json=payload)
        if response.status_code == 201:
            return response.json()
        else:
            return None
        
    def retornar(self, id) -> dict:
        response = requests.post(f'{self.BASE_URL}/posts{id}')
        if response.status_code == 200:
            return response.json()
        else:
            return None
        
    def listar(self) -> list:
        response = requests.get(f'{self.BASE_URL}/posts')
        if response.status_code == 200:
            return response.json()
        else:
            return []
        
    def modificar(self, id, titulo, corpo, user_id) -> dict:
        payload = {
            'title': titulo,
            'body': corpo,
            'userId': user_id
        }
        response = requests.put(f'{self.BASE_URL}/posts/{id}', json=payload)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def remover(self, id)  -> dict:
        response = requests.delete(f'{self.BASE_URL}/posts/{id}')
        if response.status_code == 200:
            return response.json()
        else:
            return None