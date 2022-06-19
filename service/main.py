from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from service import crud, models, schemas
from service.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/items/", response_model=List[schemas.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items


@app.get("/items/{item_id}/", response_model=schemas.Item)
def read_item(item_id: str, db: Session = Depends(get_db)):
    db_item = crud.get_item_by_id(db, item_id=item_id)
    if not db_item:
        raise HTTPException(status_code=404, detail="Item doesn't exist")
    return db_item


@app.post("/items/create_with_barcode/", response_model=schemas.Item)
def create_item_with_barcode(item: schemas.ItemCreateWithBarcode, db: Session = Depends(get_db)):
    db_item = crud.get_item_by_id(db, item_id=item.id)
    if db_item:
        raise HTTPException(status_code=400, detail="Item already exists, update the item instead")
    return crud.create_item_with_barcode(db=db, item=item)


@app.post("/items/create_without_barcode/", response_model=schemas.Item)
def create_item_without_barcode(item: schemas.ItemCreateWithoutBarcode, db: Session = Depends(get_db)):
    return crud.create_item_without_barcode(db=db, item=item)


@app.post("/items/{item_id}/update/", response_model=schemas.Item)
def update_item(item_id: str, item: schemas.ItemUpdate, db: Session = Depends(get_db)):
    db_item = crud.get_item_by_id(db, item_id=item_id)
    if not db_item:
        raise HTTPException(status_code=404, detail="Item doesn't exist")
    return crud.update_item(db=db, db_item=db_item, item_update=item)


@app.post("/items/{item_id}/delete/")
def delete_item(item_id: str, db: Session = Depends(get_db)) -> None:
    db_item = crud.get_item_by_id(db, item_id=item_id)
    if not db_item:
        raise HTTPException(status_code=404, detail="Item doesn't exist")
    crud.delete_item(db=db, item_id=item_id)
