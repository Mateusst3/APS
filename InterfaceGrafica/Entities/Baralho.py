import array as arr
import random
from Entities.Carta import Carta
from Enumerations.CorDaCarta import Cor


class Baralho:

    def __init__(self):
        self.__baralhoDeCartas = arr.array(Carta, [])

    def get_baralho_de_cartas(self):
        return self.__baralhoDeCartas
   
    def set_baralho_de_cartas(self, baralhoDeCartas):
        self.__baralhoDeCartas = baralhoDeCartas
        
    def embaralhar():
        return None
