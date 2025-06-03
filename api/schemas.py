from pydantic import BaseModel
from typing import Optional


class Character(BaseModel):
    """ Pydantic model for characters """
    id: int
    name: Optional[str] = None
    is_hero: Optional[bool] = None
    is_taken: Optional[bool] = None
    current_aim: Optional[int] = None
    hero_base_aim: Optional[int] = None    
    hero_tech: Optional[int] = None
    hero_speed: Optional[int] = None
    hero_defense: Optional[int] = None
    hero_melee: Optional[int] = None
    base_aim: Optional[int] = None    
    tech: Optional[int] = None
    speed: Optional[int] = None
    defense: Optional[int] = None
    melee: Optional[int] = None
    rank: Optional[str] = None
    on_activation: Optional[str] = None
    on_deactivation: Optional[str] = None
    during_activation: Optional[str] = None
    passive: Optional[str] = None
    actions: Optional[int] = None

    class Config:
        orm_mode = True