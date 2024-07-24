import requests
from config import Config


class UserService:
    """
    CRUD para interagir com o endpoint '/users'
    """
    
    def __init__(self, config:Config):
        self.BASE_URL = config.BASE_URL

    def criar(self, name, username, email, phone, website):
        payload = {
            'name':name,
            'username':username,
            'email':email,
            'phone':phone,
            'website':website
        }
        response = requests.post(f'{self.BASE_URL}/users', json=payload)
        if response.status_code == 201:
            return response.json()
        else:
            return None
        
    def retornar(self, id) -> dict:
        response = requests.post(f'{self.BASE_URL}/users/{id}')
        if response.status_code == 200:
            return response.json()
        else:
            return None
        
    def listar(self):
        response = requests.get(f'{self.BASE_URL}/users')
        if response.status_code == 200:
            return response.json()
        else:
            return []
        
    def modificar(self, id, name, username, email, phone, website):
        payload = {
            'name':name,
            'username':username,
            'email':email,
            'phone':phone,
            'website':website
        }
        response = requests.patch(f'{self.BASE_URL}/users/{id}', json=payload)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def remover(self, id):
        response = requests.delete(f'{self.BASE_URL}/users/{id}')
        if response.status_code == 200:
            return response.json()
        else:
            return None