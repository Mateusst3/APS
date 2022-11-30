import random
from Entities.Carta import Carta
from Entities.Time import Time
from Entities.Baralho import Baralho
from InterfaceGrafica.Entities.InterfaceImage import InterfaceImage
from InterfaceGrafica.Entities.Jogador import Jogador
from InterfaceGrafica.Enumerations.CorDaCarta import Cor
from InterfaceGrafica.Enumerations.TipoDeDica import TipoDeDica


class Mesa:

    def __init__(self):
        self.__time = Time()
        self.__estado = InterfaceImage()
        
    def setTime(self, time : Time):
        self.__time = time
        
    def getTime(self):
        return self.__time
    
    def setEstado(self, estado : InterfaceImage):
        self.__estado = estado
        
    def getEstado(self):
        return self.__estado
    
    def darDica(self, carta : Carta, tipoDeDica : TipoDeDica): 
        if self.__time.get_dicas_disponiveis() > 0:
            carta.receberDica(tipoDeDica)
            self.__time.set_dicas_disponiveis(self.__time.get_dicas_disponiveis() - 1)
            self.__estado.encerrarTurnoJogador()
        else:
            self.__estado.setMensagem("")
            
    def selecionarCarta(self, cartaSelecionada : Carta):
        self.__estado.setCartaSelecionada(cartaSelecionada)
    
    def jogarCarta(self, cartaJogada : Carta):
        podeSerJogada = self.validarCartaJogada(cartaJogada)
        if podeSerJogada:
            self.__estado.jogarCarta(cartaJogada)
            if cartaJogada.get_numero == 5:
                self.__time.recuperar_dica()
        else:
            self.__time.cometer_infracao()
            self.__estado.descartarCarta()           
            
        
    def validarCartaJogada(self, cartaJogada : Carta):
        cor = cartaJogada.get_cor()
        ultimoNumeroJogado = self.getNumeroCartaMaisAltaDaCor(cor)
        if cartaJogada.get_numero == ultimoNumeroJogado + 1:
            return True        
        return False
    
    def getNumeroCartaMaisAltaDaCor(self, cor : Cor):
        num_carta_mais_alta = 0
        for carta in self.__estado.getArea_cartas_jogadas.get_baralho_de_cartas():
            if carta.get_cor() == cor:
                num_carta_mais_alta += 1
            
        return num_carta_mais_alta
    
    def comprarCarta(self):
        self.__estado.comprarCarta()
        
    def descartarCarta(self):
        self.__estado.descartarCarta()
        
    def receber_notificacao_de_desistencia():
        #TODO implementar restart
        return
    
    def start_match(self, id : int, nomeJogadores):
        posicao = 1
        for nome in nomeJogadores:
            jogador = Jogador(nome, posicao)
            self.__estado.getJogadores().append(jogador)
            posicao += 1
        
    def avaliarFimDeJogo(self):
        self.__estado.avaliarFimDeJogo()
        #TODO implementar restart caso seja fim de jogo
        
    