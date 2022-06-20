import pandas as pd
import streamlit as st

from app.client import get_items
from app.images import get_images, render_logo

logo = get_images()["logo"]
render_logo(logo)

items = get_items()

col1, col2, col3 = st.columns([2, 6, 2])
with col2:
    df = pd.DataFrame(items).drop(columns=["id"])
    styler = df.style.hide_index()
    st.write(styler.to_html(), unsafe_allow_html=True)
