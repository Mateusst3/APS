from Time import Time
from Baralho import Baralho


class Mesa:

    def __init__(self):
        self.__time = Time()
        self.__baralhoDaMesa = None
        self.__baralhoDeCompra = None
        self.__baralhoDeDescarte = []

    def inicia_partida(self):
        return len(self.__time)

    def embaralhar(self):
        # TODO in a better notebook: uma forma de embaralhar os itens do array
        return self.__baralhoDaMesa

    def dar_cartas(self):
        return len(self.__time)

    def get_time(self):
        return self.__time

    def get_baralho_da_mesa(self):
        return self.__baralhoDaMesa

    def set_baralho_da_mesa(self):
        self.__baralhoDaMesa = Baralho(self)

    def get_baralho_de_compra(self):
        return self.__baralhoDeCompra

    def set_baralho_de_compra(self):
        self.__baralhoDaMesa = Baralho(self)

    def get_baralho_de_descarte(self):
        return self.__baralhoDeDescarte

    def set_baralho_de_descarte(self, carta):
        self.__baralhoDeDescarte.append(carta)
