from sqlalchemy import Column, Enum, Integer, String

from service.constants import AllowedCategories
from service.database import Base


class Item(Base):
    __tablename__ = "items"

    id = Column(String, primary_key=True, index=True)
    name = Column(String, index=True)
    category = Column(Enum(AllowedCategories), index=True)
    quantity = Column(Integer)
