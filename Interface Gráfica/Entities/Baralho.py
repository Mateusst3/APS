import random
from Carta import Carta
from Enums.CorDaCarta import Cor


class Baralho:

    def __init__(self, Jogador):
        self.__baralhoDeCartas = []
        self.__jogador = Jogador

    def get_baralho_de_cartas(self):
        return self.__baralhoDeCartas

    def gerar_baralho(self):
        for i in range(5):
            cor = random.randint(1, 4)
            carta = Carta(Cor(cor), random.randint(1, 5))
            self.__baralhoDeCartas.append(carta)
        return self.__baralhoDeCartas
