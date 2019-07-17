from enum import Enum

# We create this class so that any enums we create, that inherits from this
# will return the properties name when called (Basically returning the name as a value)
# Take note, implemented in unit.py

class BaseEnum(Enum):
    def _generate_next_value_(name, start, count, last_value):
        return name