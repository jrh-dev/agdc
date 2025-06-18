import streamlit as st
from dbi import DBI  # from app.dbi import DBI
import logging
import random
import base64

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

db = DBI()

@st.cache_data
def alpha_sector():
    return random.randint(1, 6)
@st.cache_data 
def bravo_sector():
    return random.randint(1, 6)
@st.cache_data
def charlie_sector():
    return random.randint(1, 6)
@st.cache_data
def delta_sector():
    return random.randint(1, 6)

def empty_sector_cache():
    """
    Clears the cached values for the sectors.
    """
    alpha_sector.clear()
    bravo_sector.clear()
    charlie_sector.clear()
    delta_sector.clear()


def gif_maker(img_path: str):
    """
    Returns the base64 encoded HR gif.
    """
    with open(img_path, "rb") as file:
        img = base64.b64encode(file.read()).decode("utf-8")
    st.markdown(
        f"""
        <style>
        .gif-container {{
            border: 2px solid #444;
            border-radius: 8px;           /* Rounded corners on the container */
            overflow: hidden;              /* Prevent the image from spilling over */
            padding: 0;
            margin: 0;
            width: 100%;
            box-sizing: border-box;
        
        .gif-container img {{
            display: block;
            width: 100%;
            height: auto;
            margin: 0;
            padding: 0;
            border-radius: 0;              /* Make sure the GIF itself has square corners */
        }}
        </style>
        <div class="gif-container">
            <img src="data:image/gif;base64,{img}" alt="hr gif">
        </div>
        """,
        unsafe_allow_html=True,
        )

@st.cache_data
def hr_gif():
    return gif_maker("images/heartrate.gif")

@st.cache_data
def motion_gif():
    return gif_maker("images/motiontracker.gif")

def check_for_rerun():
    """
    Checks if the session state has changed and reruns the app if necessary.
    """
    if "rerun" in st.session_state and st.session_state["rerun"]:
        st.session_state["rerun"] = False
        st.rerun()
        
