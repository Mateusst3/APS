

class Time:

    def __init__(self):
        self.__jogadores = []
        self.__dicasDisponiveis = 8
        self.__infracoesCometidas = 0
        self.__pontuacaoFinal = None

    def adicionar_jogador(self, jogador):
        self.__jogadores.append(jogador)

    def get_jogadores(self):
        return self.__jogadores

    def get_dicas_disponiveis(self):
        return self.__dicasDisponiveis

    def set_dicas_disponiveis(self, dicasDisponiveis: int):
        self.__dicasDisponiveis = dicasDisponiveis

    def get_dicas_disponiveis(self):
        return self.__dicasDisponiveis

    def set_infracoes_cometidas(self, infracoesCometidas: int):
        self.__infracoesCometidas = infracoesCometidas

    #TODO implementar sistema de pontuação final
