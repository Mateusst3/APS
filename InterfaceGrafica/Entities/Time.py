

class Time:

    def __init__(self):
        self.__dicasDisponiveis = 8
        self.__infracoesCometidas = 0
        self.__pontuacaoFinal = None
        self.__estaNaUltimaRodada = False
        

    def get_dicas_disponiveis(self):
        return self.__dicasDisponiveis

    def set_dicas_disponiveis(self, dicasDisponiveis: int):
        self.__dicasDisponiveis = dicasDisponiveis

    def set_infracoes_cometidas(self, infracoesCometidas: int):
        self.__infracoesCometidas = infracoesCometidas
        
    def get_infracoes_cometidas(self):
        return self.__infracoesCometidas
    
    def set_pontuacao_final(self, pontuacao : int):
        self.__pontuacaoFinal = pontuacao
        
    def get_pontuacao_final(self):
        return self.__pontuacaoFinal
    
    def set_esta_na_ultima_rodada(self, estaNaUltimaRodada : bool):
        self.__estaNaUltimaRodada = estaNaUltimaRodada
        
    def get_esta_na_ultima_rodada(self):
        return self.__estaNaUltimaRodada
    
    def recuperar_dica(self):
        self.__dicasDisponiveis += 1
        
    def cometer_infracao(self):
        self.__infracoesCometidas += 1
