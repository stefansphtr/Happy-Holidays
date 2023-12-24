from pathlib import Path
import json
import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_extras.let_it_rain import rain

# Directories and file paths
THIS_DIR = Path(__file__).parent
ASSETS = THIS_DIR / "assets"
CSS_FILE = ASSETS / "style" / "style.css"
LOTTIE_ANIMATION = ASSETS / "animation_holiday.json"

# Exception handling
if not ASSETS.exists():
    raise FileNotFoundError(f"No assets directory found at {ASSETS}")

if not CSS_FILE.exists():
    raise FileNotFoundError(f"No CSS file found at {CSS_FILE}")

if not LOTTIE_ANIMATION.exists():
    raise FileNotFoundError(f"No lottie animation found at {LOTTIE_ANIMATION}")

# Function to load and display the Lottie animation
def load_lottie_animation(file_path):
    with open(file_path, "r") as f:
        return json.load(f)

# Function to apply snowfall effect
def run_snow_animation():
    rain(emoji="❄️", font_size=20, falling_speed=7, animation_length="infinite")
    
# Funtion to get the name from query parameters
def get_person_name():
    query_params = st.experimental_get_query_params()
    return query_params.get("name", ["Friend"])[0]

# Page configuration
st.set_page_config(
    page_title="Happy Holidays",
    page_icon="🎄",
    layout="wide",
)

# Run snowfall animation
run_snow_animation()

# Apply custom CSS
with open(CSS_FILE) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Display header with personalized name
PERSON_NAME = get_person_name()
st.header(f"Happy Holidays, {PERSON_NAME}! 🎄", anchor=False)

# Display the lottie animation
lottie_animation = load_lottie_animation(LOTTIE_ANIMATION)
st_lottie(lottie_animation, key="lottie-holiday", height=400)

# Personalized holiday message
st.markdown(
    f"Dear {PERSON_NAME}, wishing you and your family a very happy holiday season filled with joy and peace 🌠 and a wonderful new year! 🎉"
)
