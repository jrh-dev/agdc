"""
Python script for the home page of the AGDC application.
This script sets up the home page of the AGDC application using Streamlit.
"""

import logging
import streamlit as st
from quotes import get_quote
from style.styles import centered_quote, custom_h1
import base64
from src.utils import check_for_rerun


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

st.set_page_config(
    page_title="AGDC", page_icon=":game_die:", initial_sidebar_state="collapsed"
)

check_for_rerun()

st.html(custom_h1("Another glorious day in the Corps", 45))

st.html(centered_quote(f'"{get_quote()}"', 200, 10))

col_1, col_2 = st.columns(2)

with col_1:
    if st.button(
        "All right, sweethearts, what are you waiting for?",
        key="start_game",
        use_container_width=True,
    ):
        st.switch_page("pages/Combat_Team_Report.py")

with col_2:
    st.button("What did you say, Hudson?", key="more-quotes", use_container_width=True)
