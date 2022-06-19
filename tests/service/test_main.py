import json
from typing import List

from sqlalchemy.orm import Session
from starlette.testclient import TestClient

from service import models, schemas
from service.constants import AllowedCategories


def test_read_empty_items(client: TestClient, empty_db: Session) -> None:
    response = client.get("/items/")
    assert response.status_code == 200
    assert len(response.json()) == 0


def test_read_populated_items(client: TestClient, mock_items: List[models.Item]) -> None:
    response = client.get("/items/")
    assert response.status_code == 200
    assert len(response.json()) > 0


def test_create_item_with_barcode(client: TestClient, empty_db: Session) -> None:
    item = schemas.ItemCreateWithBarcode(id="1234", name="foo", quantity=123, category=AllowedCategories.miscellaneous)
    response = client.post("/items/create_with_barcode/", json=item.dict())
    assert response.status_code == 200
    assert response.json() == item.dict()

    items = client.get("/items/").json()
    assert len(items) == 1
    assert items[0]["id"] == item.id


def test_create_with_fake_category_fails(client: TestClient, empty_db: Session) -> None:
    item = schemas.ItemCreateWithBarcode(
        id="1234", name="foo", quantity=123, category=AllowedCategories.non_perishables
    ).dict()
    item["category"] = "foo"
    response = client.post("/items/create_with_barcode/", json=json.dumps(item))
    assert response.status_code == 422


def test_create_item_with_barcode_fails_with_existing_item(client: TestClient, mock_items: List[models.Item]) -> None:
    item = schemas.ItemCreateWithBarcode(
        id=mock_items[0].id, name="foo", quantity=123, category=AllowedCategories.non_perishables
    )
    response = client.post("/items/create_with_barcode/", json=item.dict())
    assert response.status_code == 400
    assert "already exists" in str(response.content).lower()


def test_create_item_without_barcode(client: TestClient, empty_db: Session) -> None:
    item = schemas.ItemCreateWithoutBarcode(name="foo", quantity=123, category=AllowedCategories.baby)
    response = client.post("/items/create_without_barcode/", json=item.dict())
    assert response.status_code == 200

    items = client.get("/items/").json()
    assert len(items) == 1
    assert items[0]["name"] == item.name
    assert len(items[0]["id"]) > 10


def test_update_item(client: TestClient, mock_items: List[models.Item]) -> None:
    old_item = mock_items[0]
    updater_item = schemas.ItemUpdate(name=None, quantity=157182507)

    response = client.post(f"/items/{old_item.id}/update/", json=updater_item.dict())
    assert response.status_code == 200
    new_item = response.json()

    assert new_item["id"] == old_item.id
    assert new_item["category"] == old_item.category
    assert new_item["name"] == old_item.name
    assert new_item["quantity"] == updater_item.quantity


def test_delete_item(client: TestClient, mock_items: List[models.Item]) -> None:
    item_to_delete = mock_items[0]
    response = client.post(f"/items/{item_to_delete.id}/delete/")
    assert response.status_code == 200

    response = client.get(f"/items/{item_to_delete.id}/")
    assert response.status_code == 404
