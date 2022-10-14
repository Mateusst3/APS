class Carta:

    def __init__(self, cor, numero):
        self.__recebeuDicaDeCor = None
        self.__cor = cor
        self.__numero = numero
        self.__receuDicaDeNumero = None

    def get_cor(self):
        return self.__cor

    def self_cor(self, cor: str):
        self.__cor = cor

    def get_numero(self):
        return self.__numero

    def set_numero(self, numero: int):
        self.__numero = numero

    def get_recebeu_dica_de_cor(self):
        return self.__recebeuDicaDeCor

    def set_recebeu_dica_de_cor(self, recebeuDicaDeCor: bool):
        self.__recebeuDicaDeCor = recebeuDicaDeCor

    def get_recebeu_dica_de_numero(self):
        return self.__recebeuDicaDeNumero

    def set_recebeu_dica_de_cor(self, recebeuDicaDeNumero: bool):
        self.__receuDicaDeNumero = recebeuDicaDeNumero
