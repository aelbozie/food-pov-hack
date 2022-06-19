import cv2
import streamlit as st
from streamlit_webrtc import VideoTransformerBase, webrtc_streamer

st.markdown("# Barcode Scanner")
st.sidebar.markdown("# Barcode Scanner")


class VideoTransformer(VideoTransformerBase):
    def transform(self, frame):
        img = frame.to_ndarray(format="bgr24")

        img = cv2.cvtColor(cv2.Canny(img, 100, 200), cv2.COLOR_GRAY2BGR)

        return img


webrtc_streamer(key="example", video_transformer_factory=VideoTransformer)
