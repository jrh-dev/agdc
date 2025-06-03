import requests


class DBI:
    """class for all api interactions for streamlit app"""

    def __init__(self, url: str):
        self.url = url
        self.header = {
            "accept": "application/json",
            "Content-Type": "application/json",
        }

    def get_characters(self):
        """get all characters"""
        response = requests.get(
            f"{self.url}/characters/?skip=0&limit=100",
            headers=self.header,
            timeout=5,
        )
        if response.status_code == 200:
            return response.json()
        raise requests.HTTPError(f"Error: {response.status_code} - {response.text}")

    def get_character(self, character_id: int):
        """get a single character by id"""
        response = requests.get(
            f"{self.url}/characters/{character_id}",
            headers=self.header,
            timeout=5,
        )
        if response.status_code == 200:
            return response.json()
        raise requests.HTTPError(f"Error: {response.status_code} - {response.text}")
    
    def update_character(self, character_id: int, character: dict):
        """update a character by id"""
        json = {"id": character_id}
        json.update(character)        
        response = requests.put(
            f"{self.url}/characters/{character_id}",
            headers=self.header,
            json=json,
            timeout=5,
        )
        if response.status_code == 200:
            return response.json()
        raise requests.HTTPError(f"Error: {response.status_code} - {response.text}")
