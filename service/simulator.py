import uuid
from typing import List

import numpy as np
from sqlalchemy.orm import Session

from service import models

MOCK_ITEM_TYPES = [
    "bread",
    "rice",
    "pasta",
    "sunflower oil",
    "bananas",
    "milk",
    "cheerios",
    "coco pops",
    "tinned tomatoes",
    "tuna",
]


def generate_mock_items(max_item_types: int, max_items: int) -> List[models.Item]:
    names = np.random.choice(MOCK_ITEM_TYPES, size=min(len(MOCK_ITEM_TYPES), max_item_types), replace=False)
    items = [
        models.Item(id=str(uuid.uuid4()), name=name, category="bob", quantity=np.random.randint(low=0, high=max_items))
        for name in names
    ]
    return items


def write_mock_table(db: Session, max_item_types: int, max_items: int) -> None:
    items = generate_mock_items(max_item_types, max_items)
    db.bulk_save_objects(items)
    db.commit()
