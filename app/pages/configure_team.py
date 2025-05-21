"""
Configure team before starting the game.
"""

import logging
import streamlit as st

from app.style.styles import custom_h1


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

st.set_page_config(page_title="AGDC", page_icon=":game_die:")

st.html(custom_h1("Get ready for deployment", 45))