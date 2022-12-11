from entities.carta import Carta
from entities.time import Time
from entities.interface_image import InterfaceImage
from entities.jogador import Jogador
from Enumerations.CorDaCarta import Cor
from Enumerations.TipoDeDica import TipoDeDica


class Mesa:

    def __init__(self):
        self.__time = Time()
        self.__estado = InterfaceImage()
        
    def set_time(self, time : Time):
        self.__time = time
        
    def get_time(self):
        return self.__time
    
    def set_estado(self, estado : InterfaceImage):
        self.__estado = estado
        
    def get_estado(self):
        return self.__estado
    
    def dar_dica(self, carta : Carta, tipo_de_dica : TipoDeDica): 
        if self.__time.get_dicas_disponiveis() > 0:
            carta.receberDica(tipo_de_dica)
            self.__time.set_dicas_disponiveis(self.__time.get_dicas_disponiveis() - 1)
            self.__estado.encerrar_turno_jogador()
            return ""
        else:
            return "Não há dicas disponíveis!"
               
    def jogar_carta(self, cartaJogada : Carta):
        podeSerJogada = self.validar_carta_jogada(cartaJogada)
        if podeSerJogada:
            self.__estado.jogar_carta(cartaJogada)
            if cartaJogada.get_numero == 5:
                self.__time.recuperar_dica()
        else:
            self.__time.cometer_infracao()
            self.__estado.descartar_carta()           
            
    def validar_carta_jogada(self, cartaJogada : Carta):
        cor = cartaJogada.get_cor()
        ultimoNumeroJogado = self.get_numero_carta_mais_alta_da_cor(cor)
        if cartaJogada.get_numero() == ultimoNumeroJogado + 1:
            return True        
        return False
    
    def get_numero_carta_mais_alta_da_cor(self, cor : Cor):
        num_carta_mais_alta = 0
        for carta in self.__estado.get_area_cartas_jogadas():
            if carta.get_cor() == cor:
                num_carta_mais_alta += 1
            
        return num_carta_mais_alta
    
    def comprar_carta(self):
        self.__estado.comprar_carta()
        
    def descartar_carta(self):
        if self.__time.get_dicas_disponiveis() < 8:
            self.__estado.descartar_carta()
            return ""
        else:
            return "Não há dicas a serem recuperadas, portanto você não pode descartar nenhuma carta. Escolha outra ação."
        
    def receber_notificacao_de_desistencia():
        #TODO implementar restart
        return
    
    def start_match(self, jogadores, id : int):
        self.__estado.start_match(jogadores, id)
                
        
    def avaliarFimDeJogo(self):
        self.__estado.avaliarFimDeJogo()
        if self.__estado.get_mensagem() != "":
            pontuacao_final = len(self.__estado.get_area_cartas_jogadas())
            self.__time.set_pontuacao_final(pontuacao_final)
        
    def selecionar_carta(self, carta):
        return self.__estado.avaliar_carta_selecionada(carta)
        
        
        
    