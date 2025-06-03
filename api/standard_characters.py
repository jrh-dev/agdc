from dataclasses import dataclass

from api.character_model import Character


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
        on_activation="Reveal a card: blue take aim else recycle and draw a card",
        on_deactivation=None,
        during_activation=None,
        passive="M56 costs 1 less",
        actions=2,
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
        on_activation="Recycle any card in your hand",
        on_deactivation="Reveal a card: blue optionally put top motion card to bottom, else put a card in your hand",
        during_activation=None,
        passive=None,
        actions=2,
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
        on_activation="Recycle 2 cards and draw 1",
        on_deactivation=None,
        during_activation=None,
        passive="Once, exhaust a card to move a chracter within 4 spaces of Ripley. That chracter can reroll a failed defense roll.",
        actions=2,
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
        on_activation="May draw card",
        on_deactivation=None,
        during_activation=None,
        passive="Once, may discard from your hand to re-roll Hicks failed attack",
        actions=2,
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
        passive="after using M240 draw a card, yellow recycke 2 else move up to 2 spaces",
        actions=2,
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
        on_activation="May recycle 3 cards to grant another marine an additional action",
        on_deactivation="Draw 2 cards",
        during_activation=None,
        passive=None,
        actions=2,
    )
#
