"""
Interact with team.
"""

import logging
import streamlit as st
from dbi import DBI  # from app.dbi import DBI
from src.team_interactions import display_team, display_character # from app.src.actions import Actions
from src.utils import empty_sector_cache, check_for_rerun  # from app.src.utils import empty_sector_cache
from style.styles import custom_h1

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

db = DBI("homeassistant.local:8011")

st.set_page_config(
    page_title="AGDC", page_icon=":game_die:", initial_sidebar_state="collapsed"
)

check_for_rerun()

if "display_character" not in st.session_state or not st.session_state["display_character"]:
    st.session_state["display_character"] = None
    db.reset_all()
else:
    st.session_state["active_character_aim"] = db.get_character(
        st.session_state["display_character"]
    ).get("current_aim", 0)
    st.session_state["active_character_actions"] = db.get_character(
        st.session_state["display_character"]
    ).get("actions", 0)

st.html(custom_h1("Combat Team Report", 25))

display_team()

if st.session_state["display_character"]:
    display_character(st.session_state["display_character"])


st.write("")
bottom_col1, bottom_col2 = st.columns(2)
with bottom_col1:
    if st.button(
        "Threat Assessment",
        key="threat_assessment",
        use_container_width=True,
    ):
        st.switch_page("pages/Threat_Assessment.py")
with bottom_col2:
    if st.button(
        "End Turn",
        key="end_turn",
        use_container_width=True,
    ):
        db.reset_all()
        empty_sector_cache()
        st.session_state["action_message"] = None
        st.rerun()
