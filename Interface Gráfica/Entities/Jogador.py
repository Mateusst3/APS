from Baralho import Baralho


class Jogador:

    def __init__(self, nome):
        self.__nome = nome
        self.__maoDeCartas = Baralho(self).gerar_baralho()
        self.__jogouUltimoTurno = None

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome: str):
        self.__nome = nome

    def get_mao_de_cartas(self):
        return self.__maoDeCartas

    def get_jogou_ultimo_turno(self):
        return self.__jogouUltimoTurno

    def set_jogou_ultimo_turno(self, jogou: bool):
        self.__jogouUltimoTurno = jogou

    def jogar_descartar_carta(self, carta_jogada):
        for carta in self.__maoDeCartas:
            if carta == carta_jogada:
                self.__maoDeCartas.remove(carta)

    def comprar_carta(self, carta):
        self.__maoDeCartas.append(carta)

    #TODO implementar dar dica
