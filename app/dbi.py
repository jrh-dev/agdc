import requests


class DBI:
    """class for all api interactions for streamlit app"""

    def __init__(self, url: str = "http://192.168.68.50:8011"):
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
    
    def reset_aims(self,):
        """reset all character aims"""
        char_ids = [char["id"] for char in self.get_characters()]
        for character_id in char_ids:
            character = self.get_character(character_id)
            character["current_aim"] = character['hero_base_aim'] if character['is_hero'] else character['base_aim']
            self.update_character(character_id, character)

    def reset_actions(self,):
        """reset all character actions"""
        char_ids = [char["id"] for char in self.get_characters()]
        for character_id in char_ids:
            character = self.get_character(character_id)
            character["actions"] = 2
            self.update_character(character_id, character)

    def reset_all(self,):
        """reset all character aims and actions"""
        self.reset_aims()
        self.reset_actions()

    def reset_aim(self, character_id: int):
        """reset a single character aim"""
        character = self.get_character(character_id)
        character["current_aim"] = character['hero_base_aim'] if character['is_hero'] else character['base_aim']
        self.update_character(character_id, character)

    def reduce_aim(self, character_id: int):
        """reduce a single character aim by 1"""
        character = self.get_character(character_id)
        if character["current_aim"] > 0:
            character["current_aim"] -= 1
            self.update_character(character_id, character)
        else:
            raise ValueError("Character's current aim is already at 0.")

