from dataclasses import dataclass

from character_model import Character


@dataclass
class StandardCharacters:
    """
    Data class for standard characters.
    This class is used to define the standard characters in the game.
    """

    vasquez: Character = Character(
        name="PVT. Jenette Vasquez",
        is_hero=False,
        is_taken=False,
        current_aim=0,
        hero_base_aim=8,
        hero_tech=5,
        hero_speed=4,
        hero_defense=4,
        hero_melee=2,
        base_aim=6,
        tech=4,
        speed=4,
        defense=3,
        melee=1,
        rank="Private ^",
        on_activation="Hero - Reveal a card: blue take aim else recycle and draw a card",
        on_deactivation=None,
        during_activation=None,
        passive="M56 costs 1 less",
        actions=2,
        primary_weapon=None,
        secondary_weapon=None,
        equipment_slot_1=None,
        equipment_slot_2=None,
    )

    hudson: Character = Character(
        name="PVT. William L. Hudson",
        is_hero=False,
        is_taken=False,
        current_aim=0,
        hero_base_aim=6,
        hero_tech=7,
        hero_speed=4,
        hero_defense=6,
        hero_melee=2,
        base_aim=6,
        tech=6,
        speed=4,
        defense=5,
        melee=1,
        rank="Private ^",
        on_activation="Hero - Recycle any card in your hand",
        on_deactivation="Hero - Reveal a card: blue optionally put top motion card to bottom, else put a card in your hand",
        during_activation=None,
        passive=None,
        actions=2,
        primary_weapon=None,
        secondary_weapon=None,
        equipment_slot_1=None,
        equipment_slot_2=None
    )

    ripley: Character = Character(
        name="Ellen Ripley",
        is_hero=False,
        is_taken=False,
        current_aim=0,
        hero_base_aim=7,
        hero_tech=6,
        hero_speed=5,
        hero_defense=6,
        hero_melee=2,
        base_aim=5,
        tech=5,
        speed=4,
        defense=5,
        melee=1,
        rank="Civilian",
        on_activation="Hero - Recycle 2 cards and draw 1",
        on_deactivation=None,
        during_activation=None,
        passive="Hero - Once, exhaust a card to move a chracter within 4 spaces of Ripley. That chracter can reroll a failed defense roll.",
        actions=2,
        primary_weapon=None,
        secondary_weapon=None,
        equipment_slot_1=None,
        equipment_slot_2=None
    )

    hicks: Character = Character(
        name="CPL. Dwayne Hicks",
        is_hero=False,
        is_taken=False,
        current_aim=0,
        hero_base_aim=7,
        hero_tech=5,
        hero_speed=4,
        hero_defense=6,
        hero_melee=3,
        base_aim=6,
        tech=4,
        speed=4,
        defense=4,
        melee=2,
        rank="Corporal ^^",
        on_activation="Hero - May draw card",
        on_deactivation=None,
        during_activation=None,
        passive="Hero - Once, may discard from your hand to re-roll Hicks failed attack",
        actions=2,
        primary_weapon=None,
        secondary_weapon=None,
        equipment_slot_1=None,
        equipment_slot_2=None
    )

    frost: Character = Character(
        name="PVT. Ricco Frost",
        is_hero=False,
        is_taken=False,
        current_aim=0,
        hero_base_aim=6,
        hero_tech=6,
        hero_speed=3,
        hero_defense=5,
        hero_melee=3,
        base_aim=5,
        tech=5,
        speed=4,
        defense=4,
        melee=1,
        rank="Private ^",
        on_activation="Move up to 2 spaces",
        on_deactivation=None,
        during_activation=None,
        passive="Hero - After using M240 draw a card, yellow recycle 2 cards else move up to 2 spaces. Grunt - After using M240 draw a card, yellow or green recycle 2 cards.",
        actions=2,
        primary_weapon=None,
        secondary_weapon=None,
        equipment_slot_1=None,
        equipment_slot_2=None
    )

    gorman: Character = Character(
        name="LT. Scott Gorman",
        is_hero=False,
        is_taken=False,
        current_aim=0,
        hero_base_aim=5,
        hero_tech=6,
        hero_speed=4,
        hero_defense=4,
        hero_melee=2,
        base_aim=4,
        tech=5,
        speed=4,
        defense=4,
        melee=1,
        rank="Lieutenant |",
        on_activation="Hero - May recycle 3 cards to grant another marine an additional action",
        on_deactivation="Hero - Draw 2 cards",
        during_activation=None,
        passive=None,
        actions=2,
        primary_weapon=None,
        secondary_weapon=None,
        equipment_slot_1=None,
        equipment_slot_2=None
    )

