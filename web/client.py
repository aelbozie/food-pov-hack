from typing import Dict

import requests

HOST = "http://0.0.0.0:8000"


def get_items():
    response = requests.get(f"{HOST}/items/")
    return response.json()


def get_item(item_id: str):
    response = requests.get(f"{HOST}/items/{item_id}/")
    if response.status_code == 200:
        return response.json()


def create_item(item: Dict) -> None:
    response = requests.post(f"{HOST}/items/create_with_barcode/", json=item)
    assert response.status_code == 200


def update_item(item: Dict) -> None:
    response = requests.post(f"{HOST}/items/{item['id']}/update/", json=item)
    assert response.status_code == 200
