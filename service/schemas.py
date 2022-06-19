from typing import Optional

from pydantic import BaseModel, Field


class ItemBase(BaseModel):
    name: str
    category: str
    quantity: int = Field(gt=0)

    class Config:
        orm_mode = True


class ItemUpdate(BaseModel):
    name: Optional[str]
    category: Optional[str]
    quantity: Optional[int] = Field(..., gt=0)

    class Config:
        orm_mode = True


class Item(ItemBase):
    id: str


class ItemCreateWithoutBarcode(ItemBase):
    pass


class ItemCreateWithBarcode(ItemBase):
    id: str
