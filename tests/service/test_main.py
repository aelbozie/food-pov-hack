import pytest
from sqlalchemy.orm import Session
from starlette.testclient import TestClient

from service.main import root


@pytest.mark.asyncio
async def test_root():
    n = await root()
    assert len(n) == 1


def test_read_empty_items(client: TestClient, empty_db: Session) -> None:
    response = client.get("/items/")
    assert len(response.json()) == 0


def test_read_populated_items(client: TestClient, populated_db: Session) -> None:
    response = client.get("/items/")
    assert len(response.json()) > 0
