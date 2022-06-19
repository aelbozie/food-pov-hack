import uuid

from sqlalchemy.orm import Session

from service import models, schemas


def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()


def get_item_by_id(db: Session, item_id: str):
    return db.query(models.Item).filter(models.Item.id == item_id).first()


def create_item_with_barcode(db: Session, item: schemas.ItemCreateWithBarcode) -> models.Item:
    db_item = models.Item(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def create_item_without_barcode(db: Session, item: schemas.ItemCreateWithoutBarcode) -> models.Item:
    db_item = models.Item(id=str(uuid.uuid4()), **item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def update_item(db: Session, db_item: models.Item, item_update: schemas.ItemUpdate) -> models.Item:
    fields_to_update = item_update.dict(exclude_unset=True)  # TODO: do we want exclude_none or _unset?
    for key, value in fields_to_update.items():
        setattr(db_item, key, value)
    db.commit()
    db.refresh(db_item)
    return db_item


def delete_item(db: Session, item_id: str) -> models.Item:
    db_item = get_item_by_id(db, item_id)
    db.delete(db_item)
    db.commit()
    db.refresh(db_item)  # TODO: should we refresh here?
    return db_item
