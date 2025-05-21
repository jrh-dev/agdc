from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class Character(BaseModel):
    """ Pydantic model for characters """
    id: int
    name: str
    is_hero: bool
    is_taken: bool
    base_aim: int
    current_aim: int
    tech: int
    speed: int
    defense: int
    melee: int
    rank: int
    on_activation: Optional[str] = None
    on_deactivation: Optional[str] = None
    during_activation: Optional[str] = None
    passive: Optional[str] = None
    actions: int

    class Config:
        orm_mode = True