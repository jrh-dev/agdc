"""
A module to handle actions for characters in a game.
This module contains the ActionHandler class, which represents a character's actions.
It inherits from the Character class and provides methods to handle various actions.
"""

from api.character import Character

class ActionHandler(Character):
    """
    Class to handle actions for characters.
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
            on_activation=on_activation,
            on_deactivation=on_deactivation,
            during_activation=during_activation,
            passive=passive,
        )
        self.name = name
        self.available_actions: int = 2
        self.base_aim = aim
        self.is_taken = False

    def Move(self):
        """
        Handle the move action.
        """
        if self.available_actions > 0:
            self.use_action()
                
    def Attack(self):
        """
        Handle the attack action.
        """
        if self.available_actions > 0:
            self.use_action()
            self.reduce_aim()

    def Barricade(self):
        """
        Handle the barricade action.
        """
        if self.available_actions > 0:
            self.use_action()

    def Aim(self):
        """
        Handle the aim action.
        """
        if self.available_actions > 0:
            self.use_action()
            self.take_aim()

    def Interact(self):
        """
        Handle the interact action.
        """
        self.use_action()

    def CardAction(self):
        """
        Handle the card action.
        """
        self.use_action()

    def Rest(self):
        """
        Handle the rest action.
        """
        self.use_action()