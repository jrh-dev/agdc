from sqlalchemy.orm import Session
import character_model
from standard_characters import StandardCharacters
from dataclasses import fields


class DBI:
    """
    Class to handle database interactions.
    """

    def __init__(self, db: Session):
        self.db = db
        for f in fields(StandardCharacters):
            self.create_character(getattr(StandardCharacters, f.name))

    def get_all_characters(self, skip: int = 0, limit: int = 100):
        """
        Get all characters from the database.
        """
        return self.db.query(character_model.Character).offset(skip).limit(limit).all()

    def get_character(self, character_id: int):
        """
        Get a single character by ID.
        """
        return (
            self.db.query(character_model.Character)
            .filter(character_model.Character.id == character_id)
            .first()
        )

    def create_character(self, character: character_model.Character):
        """
        Create a new character in the database.
        """
        self.db.add(character)
        self.db.commit()
        self.db.refresh(character)
        return character

    def update_character(self, character_id: int, character: character_model.Character):
        """
        Update a character by ID.
        """
        db_character = (
            self.db.query(character_model.Character)
            .filter(character_model.Character.id == character_id)
            .first()
        )
        if db_character:
            for key, value in character.dict().items():
                setattr(db_character, key, value)
            self.db.commit()
            self.db.refresh(db_character)
        return db_character

    def delete_character(self, character_id: int):
        """
        Delete a character by ID.
        """
        db_character = (
            self.db.query(character_model.Character)
            .filter(character_model.Character.id == character_id)
            .first()
        )
        if db_character:
            self.db.delete(db_character)
            self.db.commit()
        return db_character

    def set_hero_status(self, character_id: int, is_hero: bool):
        """
        Set hero status for a character.
        """
        db_character = (
            self.db.query(character_model.Character)
            .filter(character_model.Character.id == character_id)
            .first()
        )
        if db_character:
            db_character.is_hero = is_hero
            self.db.commit()
            self.db.refresh(db_character)
        return db_character

