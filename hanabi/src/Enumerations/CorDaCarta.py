from enum import Enum


class Cor(Enum):
    red = 1
    green = 2
    blue = 3
    yellow = 4
    white = 5
    
    def __repr__(self):
            return str(self.__dict__)
