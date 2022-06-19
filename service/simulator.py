import uuid
from typing import List

import numpy as np
from sqlalchemy.orm import Session

from service import models
from service.constants import AllowedCategories

MOCK_ITEM_TYPES = {
    "tinned tomatoes": AllowedCategories.non_perishables,
    "rice": AllowedCategories.non_perishables,
    "pasta": AllowedCategories.non_perishables,
    "sunflower oil": AllowedCategories.non_perishables,
    "shampoo": AllowedCategories.toiletries,
    "hand soap": AllowedCategories.toiletries,
    "nappies": AllowedCategories.baby,
    "winter coat": AllowedCategories.miscellaneous,
}


def generate_mock_items(max_items: int) -> List[models.Item]:
    names = np.random.choice(list(MOCK_ITEM_TYPES.keys()), size=len(MOCK_ITEM_TYPES), replace=False)
    items = [
        models.Item(
            id=str(uuid.uuid4()),
            name=name,
            category=MOCK_ITEM_TYPES[name],
            quantity=np.random.randint(low=0, high=max_items),
        )
        for name in names
    ]
    return items


def write_mock_table(db: Session, max_items: int) -> List[models.Item]:
    items = generate_mock_items(max_items)
    db.bulk_save_objects(items)
    db.commit()
    return items
