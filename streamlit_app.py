from pathlib import Path
import json
import streamlit as st
import streamlit_lottie as st_lottie
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

# 