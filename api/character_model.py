"""
"""


from sqlalchemy import Column, Integer, String, Boolean
from database import Base


class Character(Base):
    """ SQLAlchemy model for characters """
    __tablename__ = "characters"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    is_hero = Column(Boolean, index=True)
    is_taken = Column(Boolean, index=True)
    current_aim = Column(Integer, index=True)
    hero_base_aim = Column(Integer, index=True)
    hero_tech = Column(Integer, index=True)
    hero_speed = Column(Integer, index=True)
    hero_defense = Column(Integer, index=True)
    hero_melee = Column(Integer, index=True)
    base_aim = Column(Integer, index=True)
    tech = Column(Integer, index=True)
    speed = Column(Integer, index=True)
    defense = Column(Integer, index=True)
    melee = Column(Integer, index=True)
    rank = Column(String, index=True)
    on_activation = Column(String, index=True, nullable=True)
    on_deactivation = Column(String, index=True, nullable=True)
    during_activation = Column(String, index=True, nullable=True)
    passive = Column(String, index=True, nullable=True)
    actions = Column(Integer, index=True)
    primary_weapon = Column(String, index=True, nullable=True)
    secondary_weapon = Column(String, index=True, nullable=True)
    equipment_slot_1 = Column(String, index=True, nullable=True)
    equipment_slot_2 = Column(String, index=True, nullable=True)

