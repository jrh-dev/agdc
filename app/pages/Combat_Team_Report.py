"""
Interact with team.
"""

import logging
import streamlit as st
from dbi import DBI  # from app.dbi import DBI
from src.team_interactions import display_team, display_character # from app.src.actions import Actions

from style.styles import custom_h1

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

db = DBI("http://localhost:8000")

st.set_page_config(
    page_title="AGDC", page_icon=":game_die:", initial_sidebar_state="collapsed"
)

if "display_character" not in st.session_state:
    st.session_state["display_character"] = None
else:
    st.session_state["active_character_aim"] = db.get_character(
        st.session_state["display_character"]
    ).get("current_aim", 0)
    st.session_state["active_character_actions"] = db.get_character(
        st.session_state["display_character"]
    ).get("actions", 0)

st.html(custom_h1("Combat Team Report", 45))

display_team()

if st.session_state["display_character"]:
    display_character(st.session_state["display_character"])

