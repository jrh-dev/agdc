import logging
from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session
from api import character_model, dbi, schemas
from api.database import SessionLocal, engine

character_model.Base.metadata.create_all(bind=engine)

router = APIRouter()


def get_db():
    """ create new session on request and closes on completion """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
async def root():
    """ Root endpoint """
    logging.info("Root endpoint accessed")
    return {"message": "Welcome to the AGDC API!"}

@router.get("/characters/", response_model=list[schemas.Character])
async def get_characters(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """ Get all characters """
    logging.info("Get all characters endpoint accessed")
    characters = dbi.DBI(db).get_all_characters(skip=skip, limit=limit)
    return characters

@router.get("/characters/{character_id}", response_model=schemas.Character)
async def get_character(character_id: int, db: Session = Depends(get_db)):
    """ Get a single character by ID """
    logging.info(f"Get character with ID {character_id} endpoint accessed")
    character = dbi.DBI(db).get_character(character_id=character_id)
    if character is None:
        raise HTTPException(status_code=404, detail="Character not found")
    return character

@router.post("/characters/", response_model=schemas.Character)
async def create_character(character: schemas.Character, db: Session = Depends(get_db)):
    """ Create a new character """
    logging.info("Create character endpoint accessed")
    db_character = dbi.DBI(db).create_character(character)
    return db_character

@router.put("/characters/{character_id}", response_model=schemas.Character)
async def update_character(character_id: int, character: schemas.Character, db: Session = Depends(get_db)):
    """ Update a character by ID """
    logging.info(f"Update character with ID {character_id} endpoint accessed")
    db_character = dbi.DBI(db).update_character(character_id=character_id, character=character)
    if db_character is None:
        raise HTTPException(status_code=404, detail="Character not found")
    return db_character

@router.delete("/characters/{character_id}", response_model=schemas.Character)
async def delete_character(character_id: int, db: Session = Depends(get_db)):
    """ Delete a character by ID """
    logging.info(f"Delete character with ID {character_id} endpoint accessed")
    db_character = dbi.DBI(db).delete_character(character_id=character_id)
    if db_character is None:
        raise HTTPException(status_code=404, detail="Character not found")
    return db_character
