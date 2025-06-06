import streamlit as st
from dbi import DBI  # from app.dbi import DBI
from src.utils import hr_gif

db = DBI("http://localhost:8000")


def set_display_character(uid: int):
    st.session_state["display_character"] = uid
    st.session_state["action_message"] = None


def make_hero():
    if uid := st.session_state["display_character"]:
        current_character = db.get_character(uid)
        current_character["is_hero"] = True
        current_character["current_aim"] = current_character.get("hero_base_aim", 0)
        db.update_character(uid, current_character)
        st.rerun()


def make_grunt():
    if uid := st.session_state["display_character"]:
        current_character = db.get_character(uid)
        current_character["is_hero"] = False
        current_character["current_aim"] = current_character.get("base_aim", 0)
        db.update_character(uid, current_character)
        st.rerun()

def toggle_taken():
    if uid := st.session_state["display_character"]:
        current_character = db.get_character(uid)
        current_character["is_taken"] = False if current_character["is_taken"] else True
        db.update_character(uid, current_character)
        st.rerun()


def display_character(uid: int):
    character = db.get_character(uid)
    is_hero = character["is_hero"]
    is_taken = character["is_taken"]
    if is_hero and not is_taken:
        status = "Hero"
    elif not is_hero and not is_taken:
        status = "Grunt"
    else:
        status = "Taken"
    if character:
        st.header(f"{character['name']}")
        st.write(":material/vital_signs: Status")     
        with st.container(border=False):
            sub_col1, sub_col2, sub_col3, sub_col4 = st.columns(4)
            with sub_col1:
                hr_gif()
            with sub_col2:
                st.metric("Status", value=status, border=True)
            with sub_col3:
                st.metric(label="Aim", value=character['current_aim'], border=True)
            with sub_col4:
                st.metric(label="Actions", value=st.session_state["active_character_actions"], border=True)

            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.metric("Tech", value=character['hero_tech'] if is_hero else character['tech'], border=True)
            with col2:
                st.metric("Speed", value=character['hero_speed'] if is_hero else character['speed'], border=True)
            with col3:
                st.metric("Defense", value=character['hero_defense'] if is_hero else character['defense'], border=True)
            with col4:
                st.metric("Melee", value=character['hero_melee'] if is_hero else character['melee'], border=True)
        st.write(":material/construction: Loadout")
        load_out()
        st.write(":material/double_arrow: Actions")
        if "display_character" in st.session_state and st.session_state["display_character"]:
            display_actions()
        
        if "action_message" in st.session_state and st.session_state["action_message"]:
            st.info(st.session_state["action_message"])
        
        st.write(":material/psychology: Abilities")
        with st.container(border=True):
            tab1, tab2, tab3, tab4 = st.tabs(["On Activation", "On Deactivation", "During Activation", "Passive"])
            with tab1:
                if character.get("on_activation"):            
                    st.write("**On Activation:**")
                    st.write(f"{character['on_activation']}")
            with tab2:
                if character.get("on_deactivation"):
                    st.write("**On Deactivation:**")
                    st.write(f"{character['on_deactivation']}")
            with tab3:
                if character.get("during_activation"):
                    st.write("**During Activation:**")
                    st.write(f"{character['during_activation']}")
            with tab4:
                if character.get("passive"):
                    st.write("**Passive:**")
                    st.write(f"{character['passive']}")
    else:
        st.error("Character not found.")


def display_team():
    characters = [c for c in db.get_characters()]
    n = len(characters)
    half = (n + 1) // 2  # split into two rows, first row gets extra if odd

    rows = [characters[:half], characters[half:]]
    for row in rows:
        cols = st.columns(len(row) if row else 1)
        for idx, character in enumerate(row):
            with cols[idx]:
                if st.button(
                    f"**{character['name']}**",
                    key=f"char_{character['id']}",
                    use_container_width=True,
                    on_click=set_display_character,
                    args=(character["id"],),
                    icon=":material/skull:" if character["is_taken"] else None,
                ):
                    st.rerun()

def display_actions():
    move, attack, barricade, aim, interact, card, rest, hero, taken = st.columns(9)

    if move.button(
        "", use_container_width=True, help="Move your character", icon=":material/explore:"
    ):
        use_action(f"Move up-to {db.get_character(st.session_state['display_character'])['speed']} spaces.")

    if attack.button(
        "", use_container_width=True, help="Fire Weapon", icon=":material/point_scan:"
    ):
        if db.get_character(st.session_state["display_character"])["actions"] > 0:
            attack_manager()
    if barricade.button(
        "", use_container_width=True, help="Barricade", icon=":material/gate:"
    ):        
        if db.get_character(st.session_state["display_character"])["actions"] > 0:
            barricade_manager()        
    if aim.button("", use_container_width=True, help="Aim", icon=":material/target:"):
        if db.get_character(st.session_state["display_character"])["actions"] > 0:
            character = db.get_character(st.session_state["display_character"])
            character["current_aim"] += 1
            db.update_character(
                st.session_state["display_character"], character
            )
        use_action("Aim increased.")
    if interact.button(
        "",
        use_container_width=True,
        help="Interact with object",
        icon=":material/touch_app:",
    ):
        use_action("Used interact action.")
    if card.button(
        "", use_container_width=True, help="Use a card", icon=":material/stacks:"
    ):
        use_action("Used a card.")
    if rest.button("", use_container_width=True, help="Rest", icon=":material/bed:"):
        use_action("Used a rest action.")
    if hero.button(
        "", use_container_width=True, help="Toggle hero status", icon=":material/military_tech:"
    ):
        make_hero() if not db.get_character(st.session_state["display_character"])["is_hero"] else make_grunt()
    if taken.button(
        "", use_container_width=True, help="Taken", icon=":material/skull:"
    ):
        toggle_taken()

def _dice_roll():
    import random
    return random.randint(0, 9)


@st.dialog("Attack")
def attack_manager():
    st.segmented_control("Select weapon", ["Primary", "secondary"], selection_mode="single")
        
    aim = db.get_character(st.session_state["display_character"])["current_aim"]
    row_1_col1, row_1_col2 = st.columns(2)
    with row_1_col1:
        st.checkbox("Full Auto", value=False, help="Use full auto mode")
    with row_1_col2:
        roll_two = st.checkbox("Roll Two", value=False, help="Roll two dice and take the best result")

    if aim > 0:
        roll_button_col1, roll_button_col2 = st.columns(2)
        with roll_button_col1:
            roller = st.button("Fire", use_container_width=True, on_click=db.reduce_aim, args=(st.session_state["display_character"],))
        with roll_button_col2:
            manual_roller = st.button("Manual Roll", use_container_width=True, help="Roll manually", on_click=db.reduce_aim, args=(st.session_state["display_character"],))
    else:
        roller = None
        manual_roller = None
        st.markdown(
            "You have no aim left, you cannot fire. Use the **Aim** action to gain aim."
        )

    if manual_roller:
        st.info("""
                Roll the dice. \n\n
                "I can't lie to you about your chances, but you have my sympathies".
                """)

    row_2_col1, row_2_col2 = st.columns(2)
    with row_2_col1:
        if roller:
            d1 = _dice_roll()
            st.write(f"Rolled: {d1}")
            st.metric("Dice 1", f"{'Hit' if d1 <= aim else 'Miss'}")
    with row_2_col2:
        if roller and roll_two:
            d2 = _dice_roll()
            st.write(f"Rolled: {d2}")
            st.metric("Dice 2", f"{'Hit' if d2 <= aim else 'Miss'}")

    if st.button("End Attack", use_container_width=True):
        use_action()
        st.rerun()


@st.dialog("Barricade")
def barricade_manager():
    tech = db.get_character(st.session_state["display_character"])["hero_tech" if db.get_character(st.session_state["display_character"])["is_hero"] else "tech"]
    st.metric("Barricade attempt:", f"{'Successful' if _dice_roll() <= tech else 'Failed'}")
    if st.button("Close", use_container_width=True):
        use_action()
        st.session_state["rerun"] = True

@st.dialog("Defense Role")
def defense_manager():
    defense = db.get_character(st.session_state["display_character"])["hero_defense" if db.get_character(st.session_state["display_character"])["is_hero"] else "defense"]
    melee = db.get_character(st.session_state["display_character"])["hero_melee" if db.get_character(st.session_state["display_character"])["is_hero"] else "melee"]
    rolled = _dice_roll()
    st.write(f"Rolled: {rolled}")
    st.metric("Defense:", f"{'Successful' if rolled <= defense else 'Failed'}")
    st.metric("Counterattack:", f"{'Successful' if rolled <= melee else 'Failed'}")

def use_action(message=None):
    if uid := st.session_state["display_character"]:
        character = db.get_character(uid)
        character["actions"] -= 1
        if character["actions"] >= 0:
            db.update_character(uid, character)
            st.session_state["active_character_actions"] = character["actions"]
            st.session_state["action_message"] = f"""
                {message if message else ''}
                {'\n\n' if message else ''}
                Remaining actions: {character['actions']}
            """
        else:
            st.session_state["action_message"] = "No actions left."        
        st.rerun()

def move_character():
    if uid := st.session_state["display_character"]:
        character = db.get_character(uid)
        if character["is_hero"]:
            message = f"Move upto {character['hero_speed']} spaces."
        else:
            message = f"Move upto {character['speed']} spaces."
        use_action(uid, message)


def available_weapons() -> list:
    return ["M41A Pulse Rifle", "M240 Flamethrower", "M56 Smartgun", "HK VP70 Pistol", "M40 Grenades",]

def available_equipment() -> list:
    return ["Hadley's Hope Map", "Flare", "Shoulder Lamp", "Arc Welder", "Body Armor", "Motion Tracker", "Medical Scanner", "M4 Helmet"]

@st.dialog("Choose Primary Weapon")
def assign_primary_weapon():
    if uid := st.session_state["display_character"]:
        character = db.get_character(uid)
        selected_weapon = st.selectbox(
            "Select Primary Weapon",
            options=available_weapons(),
            index=None,
            key="primary_weapon_select",
        )
        if st.button("Close", use_container_width=True):
            character["primary_weapon"] = selected_weapon
            db.update_character(uid, character)
            st.rerun()

@st.dialog("Choose Secondary Weapon")
def assign_secondary_weapon():
    if uid := st.session_state["display_character"]:
        character = db.get_character(uid)
        selected_weapon = st.selectbox(
            "Select Secondary Weapon",
            options=available_weapons(),
            index=None,
            key="secondary_weapon_select",
        )
        if st.button("Close", use_container_width=True):
            character["secondary_weapon"] = selected_weapon
            db.update_character(uid, character)
            st.rerun()

@st.dialog("Choose Equipment Slot 1")
def assign_equipment_slot_1():
    if uid := st.session_state["display_character"]:
        character = db.get_character(uid)
        selected_equipment = st.selectbox(
            "Select Equipment Slot 1",
            options=available_equipment(),
            index=None,
            key="equipment_slot_1_select",
        )
        if st.button("Close", use_container_width=True):
            character["equipment_slot_1"] = selected_equipment
            db.update_character(uid, character)
            st.rerun()

@st.dialog("Choose Equipment Slot 2")
def assign_equipment_slot_2():
    if uid := st.session_state["display_character"]:
        character = db.get_character(uid)
        selected_equipment = st.selectbox(
            "Select Equipment Slot 2",
            options=available_equipment(),
            index=None,
            key="equipment_slot_2_select",
        )
        if st.button("Close", use_container_width=True):
            character["equipment_slot_2"] = selected_equipment
            db.update_character(uid, character)
            st.rerun()

def display_primary_weapon():
    if uid := st.session_state["display_character"]:
        character = db.get_character(uid)
        primary_weapon = character.get("primary_weapon", None)
        if st.button(
            f"{primary_weapon if primary_weapon else 'Empty'}",
            use_container_width=True,
            key="primary_weapon_button",
        ):
            assign_primary_weapon()

def display_secondary_weapon():
    if uid := st.session_state["display_character"]:
        character = db.get_character(uid)
        secondary_weapon = character.get("secondary_weapon", None)
        if st.button(
            f"{secondary_weapon if secondary_weapon else 'Empty'}",
            use_container_width=True,
            key="secondary_weapon_button",
        ):
            assign_secondary_weapon()

def display_equipment_slot_1():
    if uid := st.session_state["display_character"]:
        character = db.get_character(uid)
        equipment_slot_1 = character.get("equipment_slot_1", None)
        if st.button(
            f"{equipment_slot_1 if equipment_slot_1 else 'Empty'}",
            use_container_width=True,
            key="equipment_slot_1_button",
        ):
            assign_equipment_slot_1()

def display_equipment_slot_2():
    if uid := st.session_state["display_character"]:
        character = db.get_character(uid)
        equipment_slot_2 = character.get("equipment_slot_2", None)
        if st.button(
            f"{equipment_slot_2 if equipment_slot_2 else 'Empty'}",
            use_container_width=True,
            key="equipment_slot_2_button",
        ):
            assign_equipment_slot_2()

def load_out():
    if st.session_state["display_character"]:
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            display_primary_weapon()
        with col2:
            display_secondary_weapon()
        with col3:
            display_equipment_slot_1()
        with col4:
            display_equipment_slot_2()