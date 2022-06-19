from typing import List

import pytest
from sqlalchemy.orm import Session
from starlette.testclient import TestClient

from service import models
from service.database import DB_FILE, SessionLocal, engine
from service.main import app
from service.simulator import write_mock_table

test_client = TestClient(app)


def delete_db() -> None:
    assert DB_FILE.parent.exists()
    try:
        DB_FILE.unlink()
    except FileNotFoundError:
        pass


def initialise_db() -> Session:
    delete_db()
    db = SessionLocal()
    models.Base.metadata.create_all(bind=engine)
    return db


def teardown_db(db: Session) -> None:
    db.close()
    delete_db()


@pytest.fixture()
def empty_db() -> Session:
    db = initialise_db()
    yield db
    teardown_db(db)


@pytest.fixture()
def mock_items(empty_db: Session) -> List[models.Item]:
    mock_items = write_mock_table(empty_db, max_item_types=10, max_items=100)
    return mock_items


@pytest.fixture()
def client() -> TestClient:
    yield test_client
