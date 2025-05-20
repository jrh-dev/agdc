"""
Module to define the Character class and its methods.
This module contains the Character class, which represents a character AGDC.
"""

from typing import Optional, Tuple

class BaseCharacter:
    """
    Base class for character AGDC.
    """

    def __init__(
        self,
        is_hero: bool,
        aim: int,
        tech: int,
        speed: int,
        defense: int,
        melee: int,
        rank: int,
        on_activation: Optional[str] = None,
        on_deactivation: Optional[str] = None,
        during_activation: Optional[str] = None,
        passive: Optional[str] = None,
        actions: Tuple[str] = Actions,
    ):
        """
        Initialize the character with the given attributes.

        Args:
            is_hero (bool): Whether the character is a hero.
            aim (int): The aim of the character.
            tech (int): The tech of the character.
            speed (int): The speed of the character.
            defense (int): The defense of the character.
            melee (int): The melee of the character.
            rank (int): The rank of the character.
            on_activation (Optional[str]): Action on activation.
            on_deactivation (Optional[str]): Action on deactivation.
            during_activation (Optional[str]): Action during activation.
            passive (Optional[str]): Passive ability.
        """
        self.is_hero = is_hero
        self.aim = aim
        self.tech = tech
        self.speed = speed
        self.defense = defense
        self.melee = melee
        self.rank = rank
        self.on_activation = on_activation
        self.on_deactivation = on_deactivation
        self.during_activation = during_activation
        self.passive = passive
        self.actions = actions

    def __str__(self):
        """
        String representation of the character.
        """
        return f"Character(is_hero={self.is_hero}, aim={self.aim}, tech={self.tech}, speed={self.speed}, defense={self.defense}, melee={self.melee}, rank={self.rank})"

    def __repr__(self):
        """
        String representation of the character for debugging.
        """
        return f"BaseCharacter(is_hero={self.is_hero}, aim={self.aim}, tech={self.tech}, speed={self.speed}, defense={self.defense}, melee={self.melee}, rank={self.rank})"


class Character(BaseCharacter):
    """
    Class representing a character AGDC.
    """

    def __init__(
        self,
        name,
        aim,
        tech,
        speed,
        defense,
        melee,
        rank,
        is_hero=False,
        on_activation=None,
        on_deactivation=None,
        during_activation=None,
        passive=None,
        actions: int = 2,
    ):
        """
        Initialize the character with the given name.

        Args:
            name (str): The name of the character.
        """
        super().__init__(
            is_hero,
            aim,
            tech,
            speed,
            defense,
            melee,
            rank,
            on_activation,
            on_deactivation,
            during_activation,
            passive,
        )

    def make_hero(self):
        """
        Make the character a hero.
        """
        self.is_hero = True

    def remove_hero(self):
        """
        Make the character a hero.
        """
        self.is_hero = False

    def was_taken(self):
        """
        Mark the character as taken.
        """
        self.is_taken = True

    def rescued(self):
        """
        Mark the character as not taken.
        """
        self.is_taken = False

    def reset_aim(self):
        """
        Reset the aim of the character.
        """
        self.aim = self.base_aim

    def reduce_aim(self):
        """
        Reduce the aim of the character by 1.
        """
        if self.aim > 0:
            self.aim -= 1

    def take_aim(self):
        """
        Take aim with the character.
        """
        self.aim += 1

    def available_actions(self) -> Tuple[str]:
        """
        Get the actions for the character.
        """
        return self.actions
    
    def use_action(self, action: str):
        """
        Use an action for the character.
        """
        if action in self.actions and self.actions > 0:
            self.actions -= 1
            # Perform the action here
        else:
            print(f"{action} is not available for {self.name}.")

    def reset_actions(self):
        """
        Reset the available actions for the character.
        """
        self.actions = 2

    def __str__(self):
        """
        String representation of the character.
        """
        return f"Character(name={self.name}, is_hero={self.is_hero}, aim={self.aim}, tech={self.tech}, speed={self.speed}, defense={self.defense}, melee={self.melee}, rank={self.rank})"

    def __repr__(self):
        """
        String representation of the character for debugging.
        """
        return f"Character(name={self.name}, is_hero={self.is_hero}, aim={self.aim}, tech={self.tech}, speed={self.speed}, defense={self.defense}, melee={self.melee}, rank={self.rank})"
