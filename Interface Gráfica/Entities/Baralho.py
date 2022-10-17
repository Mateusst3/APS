import random
from Entities.Carta import Carta
from Enums.CorDaCarta import Cor


class Baralho:

    def __init__(self, Jogador):
        self.__baralhoDeCartas = []
        self.__jogador = Jogador
        self.__cores = ["Green", "Blue", "Yellow", "Red"]

    def get_baralho_de_cartas(self):
        return self.__baralhoDeCartas

    def gerar_baralho(self):
        for i in range(5):
            corNumero = random.randint(0, 3)
            carta = Carta(self.__cores[corNumero], random.randint(1, 5))
            self.__baralhoDeCartas.append(carta)
        return self.__baralhoDeCartas
