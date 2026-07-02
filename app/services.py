import requests
from app.models import User

class UserService:
    def __init__(self, api_client):
        self.api_client = api_client

    def get_user(self, user_id):
        response = self.api_client.get(f"/users/{user_id}")
        if response.status_code == 200:
            data = response.json()
            return User(**data)
        else:
            return None
