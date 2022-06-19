import av
import cv2
import streamlit as st
from pyzbar import pyzbar

from streamlit_webrtc import webrtc_streamer, VideoProcessorBase

st.markdown("# Barcode Scanner")
st.sidebar.markdown("# Barcode Scanner")


def draw_barcode(decoded, image):
    # n_points = len(decoded.polygon)
    # for i in range(n_points):
    #     image = cv2.line(image, decoded.polygon[i], decoded.polygon[(i+1) % n_points], color=(0, 255, 0), thickness=5)
    # uncomment above and comment below if you want to draw a polygon and not a rectangle
    image = cv2.rectangle(image, (decoded.rect.left, decoded.rect.top),
                          (decoded.rect.left + decoded.rect.width, decoded.rect.top + decoded.rect.height),
                          color=(0, 255, 0),
                          thickness=5)
    return image


def decode(image):
    # decodes all barcodes from an image
    decoded_objects = pyzbar.decode(image)
    for obj in decoded_objects:
        # draw the barcode
        print("detected barcode:", obj)
        image = draw_barcode(obj, image)
        # print barcode type & data
        print("Type:", obj.type)
        print("Data:", obj.data)
        print()

    return image


class VideoTransformer(VideoProcessorBase):
    def recv(self, frame):
        img = av.VideoFrame.to_ndarray(frame, format="gray8")

        # img = cv2.cvtColor(cv2.Canny(img, 100, 200), cv2.COLOR_GRAY2BGR)
        img = decode(img)

        return av.VideoFrame.from_ndarray(img, format="gray8")


webrtc_streamer(key="example", video_processor_factory=VideoTransformer)
