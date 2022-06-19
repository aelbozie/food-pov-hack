from enum import Enum


class AllowedCategories(str, Enum):
    non_perishables = "Non-perishables"
    toiletries = "Toiletries"
    household = "Household"
    baby = "Baby"
    miscellaneous = "Miscellaneous"
