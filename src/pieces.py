from enum import Enum, auto

class Pieces(Enum):
    X = auto()
    O = auto()

    def __str__(self):
        return self.name
