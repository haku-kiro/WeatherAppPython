from enum import auto, unique

# book had a period before the base_enum, like '.base_enum' ?
from base_enum import BaseEnum

@unique
class Unit(BaseEnum):
    CELSIUS = auto()
    FAHRENHEIT = auto()