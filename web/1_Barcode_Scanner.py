from hashlib import sha256

import cv2
import numpy as np
import streamlit as st
from PIL import Image
from pyzbar import pyzbar

from service.constants import AllowedCategories
from web.client import create_item, get_item, update_item
from web.images import get_images, render_logo

logo = get_images()["logo"]
render_logo(logo)

allowed_categories = [str(e) for e in AllowedCategories]


def draw_bbox(decoded, image):
    image = cv2.rectangle(
        image,
        (decoded.rect.left, decoded.rect.top),
        (decoded.rect.left + decoded.rect.width, decoded.rect.top + decoded.rect.height),
        color=(0, 255, 0),
        thickness=5,
    )
    return image


def decode(image):
    decoded_objects = pyzbar.decode(image)
    return max(decoded_objects, key=lambda x: x.quality) if decoded_objects else None


img_file_buffer = st.camera_input("Take a picture")

if img_file_buffer is not None:
    img = np.array(Image.open(img_file_buffer))
    img_bw = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    decoded = decode(img_bw)
    if decoded:
        img = draw_bbox(decoded, img)
        detected_item_id = sha256(decoded.data).hexdigest()[:16]
        existing_item = get_item(detected_item_id)
        if not existing_item:
            new_item = {
                "name": st.text_input(label="Name"),
                "category": st.selectbox(label="Category", options=allowed_categories),
                "quantity": st.number_input(label="Quantity", min_value=0, step=1),
            }
            if st.button("Submit"):
                new_item["id"] = detected_item_id
                create_item(new_item)
                st.text("✅ Added!")
        else:
            item_to_update = {
                "name": st.text_input(label="Name", value=existing_item["name"]),
                "category": st.selectbox(
                    label="Category",
                    options=allowed_categories,
                    index=allowed_categories.index(existing_item["category"]),
                ),
                "quantity": st.number_input(label="Quantity", min_value=0, step=1, value=existing_item["quantity"]),
            }
            if st.button("Update"):
                item_to_update["id"] = existing_item["id"]
                update_item(item_to_update)
                st.text("✅ Updated!")
    else:
        st.write("Nothing detected")
