import streamlit as st
from streamlit_webrtc import webrtc_streamer

st.markdown("# Barcode Scanner")
st.sidebar.markdown("# Barcode Scanner")

webrtc_streamer(key="example")
