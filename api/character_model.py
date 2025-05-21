"""
"""


from sqlalchemy import Column, Integer, String, Boolean
from api.database import Base


class Character(Base):
    """ SQLAlchemy model for characters """
    __tablename__ = "characters"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    is_hero = Column(Boolean, index=True)
    is_taken = Column(Boolean, index=True)
    base_aim = Column(Integer, index=True)
    current_aim = Column(Integer, index=True)
    tech = Column(Integer, index=True)
    speed = Column(Integer, index=True)
    defense = Column(Integer, index=True)
    melee = Column(Integer, index=True)
    rank = Column(Integer, index=True)
    on_activation = Column(String, index=True, nullable=True)
    on_deactivation = Column(String, index=True, nullable=True)
    during_activation = Column(String, index=True, nullable=True)
    passive = Column(String, index=True, nullable=True)
    actions = Column(Integer, index=True)


class Equipment(Base):
    """ SQLAlchemy model for Equipment """
    __tablename__ = "equipment"

    id = Column(Integer, primary_key=True, index=True)
    m4a1_pulse_rifle = Column(Boolean, index=True)
    ithaca_37_shotgun = Column(Boolean, index=True)
    m4_helmet = Column(Boolean, index=True)
    body_armor = Column(Boolean, index=True)
    
