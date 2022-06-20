from enum import Enum


class AllowedCategories(str, Enum):
    food_cupboard = "Food cupboard"
    toiletries = "Toiletries"
    household = "Household"
    baby = "Baby"
    miscellaneous = "Miscellaneous"

    def __str__(self) -> str:
        return str(self.value)
