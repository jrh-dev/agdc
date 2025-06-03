class Actions:
    @staticmethod
    def move(character):
        """Move action for a character."""
        if character["is_hero"]:
            return f"Move upto {character['hero_speed']} spaces."
        return f"Move upto {character['speed']} spaces."
    @staticmethod
    def attack(character):
        """Attack action for a character."""
        if character["is_hero"]:
            return f"Attack with hero's weapon."
        return f"Attack with grunt's weapon."
    @staticmethod
    def barricade(character):
        """Barricade action for a character."""
        if character["is_hero"]:
            return f"Barricade for {character['hero_tech']}."
        return f"Barricade for {character['tech']}."
    @staticmethod
    def aim(character):
        """Aim action for a character."""
        if character["is_hero"]:
            return f"Aim with hero's weapon."
        return f"Aim with grunt's weapon."
    @staticmethod
    def interact(character):
        """Interact action for a character."""
        if character["is_hero"]:
            return f"Interact with hero's ability."
        return f"Interact with grunt's ability."
    @staticmethod
    def card(character):
        """Use a card action for a character."""
        if character["is_hero"]:
            return f"Use hero's card."
        return f"Use grunt's card."
    @staticmethod
    def rest(character):
        """Rest action for a character."""
        if character["is_hero"]:
            return f"Rest to regain hero's actions."
        return f"Rest to regain grunt's actions."