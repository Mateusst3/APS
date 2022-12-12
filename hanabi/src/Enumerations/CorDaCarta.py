from enum import Enum


class Cor(Enum):
    red = 1
    green = 2
    blue = 3
    yellow = 4
    white = 5
    
    def __repr__(self):
            return str(self.__dict__)
        
    def get_enum(self, index):
        for cor in Cor:
            if cor.value == index:
                return cor
        return None
