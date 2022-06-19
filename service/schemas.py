from typing import Optional

from pydantic import BaseModel, Field

from service.constants import AllowedCategories


class ItemBase(BaseModel):
    name: str
    category: AllowedCategories
    quantity: int = Field(ge=0)

    class Config:
        orm_mode = True


class ItemUpdate(BaseModel):
    name: Optional[str]
    category: Optional[AllowedCategories]
    quantity: Optional[int] = Field(..., ge=0)

    class Config:
        orm_mode = True


class Item(ItemBase):
    id: str


class ItemCreateWithoutBarcode(ItemBase):
    pass


class ItemCreateWithBarcode(ItemBase):
    id: str
