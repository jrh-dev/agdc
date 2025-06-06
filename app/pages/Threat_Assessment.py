"""
What're those pesky aliens up to? Let's find out!
"""

import logging
import random
import streamlit as st
from dbi import DBI  # from app.dbi import DBI
from style.styles import custom_h1
from src.utils import alpha_sector, bravo_sector, charlie_sector, delta_sector, empty_sector_cache, motion_gif, check_for_rerun
from src.team_interactions import attack_manager, defense_manager  # from app.src.team_interactions import attack_manager, defense_manager

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

db = DBI("http://localhost:8000")

st.set_page_config(
    page_title="AGDC", page_icon=":game_die:", initial_sidebar_state="collapsed"
)

check_for_rerun()

st.html(custom_h1("Threat Assessment", 25))

section_col1, section_col2 = st.columns(2)
with section_col1:
    with st.container(border=False):        
        header_col1, header_col2 = st.columns(2)
        upper_col_1, upper_col_2 = st.columns(2)
        lower_col_1, lower_col_2 = st.columns(2)
        with header_col1:
            st.metric("Xenomorph Activity", value=6, border=True)
        with header_col2:
            motion_gif()
        with upper_col_1:
            st.metric("Alpha Sector Activity", value=alpha_sector(), border=True)
        with upper_col_2:
            st.metric("Bravo Sector Activity", value=bravo_sector(), border=True)
        with lower_col_1:
            st.metric("Charlie Sector Activity", value=charlie_sector(), border=True)
        with lower_col_2:
            st.metric("Delta Sector Activity", value=delta_sector(), border=True)
with section_col2:
    with st.container(border=True):
        character_dict = {}
        for c in db.get_characters():
            character_dict[c["name"]] = c["id"]
        selected_squad = st.selectbox(
            "Squad Member",
            options=character_dict.keys(),
            index=None,
            key="selected_character",
        )
        if selected_squad:
            st.session_state['display_character'] = character_dict[st.session_state['selected_character']]
            if 'selected_character' in st.session_state and st.session_state['selected_character']:
                if st.button("Defensive fire", use_container_width=True):
                    attack_manager()
                if st.button("Defensive roll", use_container_width=True):
                    defense_manager()

st.write("")
bottom_col1, bottom_col2 = st.columns(2)
with bottom_col1:
    if st.button(
        "Combat Team Report",
        key="combat_team",
        use_container_width=True,
    ):
        st.switch_page("pages/Combat_Team_Report.py")
with bottom_col2:
    if st.button(
        "End Turn",
        key="end_turn",
        use_container_width=True,
    ):
        db.reset_all()
        empty_sector_cache()
        st.session_state["action_message"] = None
        st.session_state["rerun"] = True
        st.switch_page("pages/Combat_Team_Report.py")



