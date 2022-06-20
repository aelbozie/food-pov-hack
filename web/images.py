from pathlib import Path

import numpy as np
import streamlit as st
from PIL import Image

from service.constants import AllowedCategories

RESOURCES_DIR = Path(__file__).resolve().parents[1] / "resources"

image_files = {
    "logo": RESOURCES_DIR / "logo.png",
    AllowedCategories.food_cupboard: RESOURCES_DIR / "food.png",
    AllowedCategories.toiletries: RESOURCES_DIR / "toilet.png",
    AllowedCategories.household: RESOURCES_DIR / "household.png",
    AllowedCategories.baby: RESOURCES_DIR / "baby.png",
    AllowedCategories.miscellaneous: RESOURCES_DIR / "misc.png",
}


@st.cache()
def get_images():
    images = {}
    for name, file in image_files.items():
        images[name] = np.array(Image.open(str(file)))
    return images


def render_logo(logo):
    col1, col2, col3 = st.columns([6, 6, 6])

    with col2:
        st.image(logo)
