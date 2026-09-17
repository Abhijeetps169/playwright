import requests

class UserApi:

    def create_user(self, payload):
        return requests.post(
            "/users",
            json=payload
        )