import streamlit as st
from dbi import DBI  # from app.dbi import DBI
from src.actions import Actions  # from app.src.actions import Actions

db = DBI("http://localhost:8000")


def set_display_character(uid: int):
    st.session_state["display_character"] = uid


def make_hero():
    if uid := st.session_state["display_character"]:
        current_character = db.get_character(uid)
        current_character["is_hero"] = True
        db.update_character(uid, current_character)


def make_grunt():
    if uid := st.session_state["display_character"]:
        current_character = db.get_character(uid)
        current_character["is_hero"] = False
        db.update_character(uid, current_character)


def display_character(uid: int):
    character = db.get_character(uid)
    is_hero = character["is_hero"]
    if character:
        st.subheader(f"{character['name']}")
        sub_col1, sub_col2, sub_col3, sub_col4 = st.columns(4)
        with sub_col1:
            st.metric("Status", value="Hero" if is_hero else "Grunt")
        with sub_col2:
            st.metric(label="Aim", value=character['current_aim'])
        with sub_col3:
            st.metric(label="Actions", value=st.session_state["active_character_actions"])
        with sub_col4:
            st.empty()  # Placeholder for alignment
        
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Tech", value=character['hero_tech'] if is_hero else character['tech'])
        with col2:
            st.metric("Speed", value=character['hero_speed'] if is_hero else character['speed'])
        with col3:
            st.metric("Defense", value=character['hero_defense'] if is_hero else character['defense'])
        with col4:
            st.metric("Melee", value=character['hero_melee'] if is_hero else character['melee'])

        if character.get("on_activation"):
            st.write("**On Activation:**")
            st.write(f"{character['on_activation']}")
        if character.get("on_deactivation"):
            st.write("**On Deactivation:**")
            st.write(f"{character['on_deactivation']}")
        if character.get("during_activation"):
            st.write("**During Activation:**")
            st.write(f"{character['during_activation']}")
        if character.get("passive"):
            st.write("**Passive:**")
            st.write(f"{character['passive']}")
    else:
        st.error("Character not found.")


def display_team():
    characters = [c for c in db.get_characters() if not c["is_taken"]]
    n = len(characters)
    half = (n + 1) // 2  # split into two rows, first row gets extra if odd

    rows = [characters[:half], characters[half:]]
    for row in rows:
        cols = st.columns(len(row) if row else 1)
        for idx, character in enumerate(row):
            with cols[idx]:
                st.button(
                    f"**{character['name']}**",
                    key=f"char_{character['id']}",
                    use_container_width=True,
                    on_click=set_display_character,
                    args=(character["id"],),
                )
    move, attack, barricade, aim, interact, card, rest, hero = st.columns(8)

    if move.button(
        "", use_container_width=True, help="Move your character", icon=":material/explore:"
    ):
        use_action(Actions.move)
    if attack.button(
        "", use_container_width=True, help="Fire Weapon", icon=":material/point_scan:"
    ):
        use_action(Actions.attack)
    if barricade.button(
        "", use_container_width=True, help="Barricade", icon=":material/gate:"
    ):
        use_action(Actions.barricade)
    if aim.button("", use_container_width=True, help="Aim", icon=":material/target:"):
        use_action(Actions.aim)
    if interact.button(
        "",
        use_container_width=True,
        help="Interact with object",
        icon=":material/touch_app:",
    ):
        use_action(Actions.interact)
    if card.button(
        "", use_container_width=True, help="Use a card", icon=":material/stacks:"
    ):
        use_action(Actions.card)
    if rest.button("", use_container_width=True, help="Rest", icon=":material/bed:"):
        use_action(Actions.rest)
    if hero.button(
        "", use_container_width=True, help="Toggle hero status", icon=":material/military_tech:"
    ):
        make_hero() if not db.get_character(st.session_state["display_character"])["is_hero"] else make_grunt()


def use_action(message):
    if uid := st.session_state["display_character"]:
        character = db.get_character(uid)
        message_return = message(character)
        character["actions"] -= 1
        if character["actions"] >= 0:
            db.update_character(uid, character)
            st.session_state["active_character_actions"] = character["actions"]
            st.success(
                f"""
                {message_return}\n\n
                Remaining actions: {character['actions']}
                """
            )
        else:
            st.error("No actions left.")

def move_character():
    if uid := st.session_state["display_character"]:
        character = db.get_character(uid)
        if character["is_hero"]:
            message = f"Move upto {character['hero_speed']} spaces."
        else:
            message = f"Move upto {character['speed']} spaces."
        use_action(uid, message)
