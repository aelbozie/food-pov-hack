from enum import Enum


class Tables(str, Enum):
    MOCK_INVENTORY = "mock_inventory"
    INVENTORY = "inventory"

    def __str__(self) -> str:
        return str(self.value)
