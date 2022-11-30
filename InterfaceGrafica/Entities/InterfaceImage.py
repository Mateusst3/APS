import array as arr
import random
from Entities.Baralho import Baralho
from Enumerations.StatusPartida import StatusPartida
from InterfaceGrafica.Entities.Carta import Carta
from InterfaceGrafica.Entities.Jogador import Jogador
from InterfaceGrafica.Enumerations.CorDaCarta import Cor


class InterfaceImage:
    def __init__(self):
        self.__mensagem = '' 
        self.__area_cartas_jogadas = Baralho()
        self.__area_descarte = Baralho()
        self.__area_compra = Baralho()
        self.__status = StatusPartida.AGUARDANDO_INICIO
        self.__jogadores = arr.array(Jogador, [])
        self.__carta_selecionada = None
        
    def setMensagem(self, mensagem):
        self.__mensagem = mensagem
        
    def getMensagem(self): 
        return self.__mensagem
    
    def setArea_cartas_jogadas(self, baralho : Baralho):
        self.__area_cartas_jogadas = baralho
    
    def getArea_cartas_jogadas(self):
        return self.__area_cartas_jogadas
    
    def setArea_descarte(self, baralho : Baralho):
        self.__area_descarte = baralho
        
    def getArea_descarte(self):
        return self.__area_descarte
    
    def setArea_compra(self, baralho : Baralho):
        self.__area_compra = baralho
        
    def getArea_compra(self):
        return self.__area_compra
    
    def setStatus(self, status):
        self.__status = status
        
    def getStatus(self):
        return self.__status
    
    def setJogadores(self, jogadores):
        self.__jogadores = jogadores
        
    def getJogadores(self):
        return self.__jogadores
    
    def setCartaSelecionada(self, carta : Carta):
        self.__carta_selecionada = carta
        
    def getCarta_selecionada(self):
        return self.__carta_selecionada
       
    def constroiBaralhoInicial(self):
        baralho_compra = self.getArea_compra().get_baralho_de_cartas()
        for i in range (1,6): #numero
            for j in range (1,6): #cor
                baralho_compra.append(Carta(Cor(j), i))
                if i == 1:
                    baralho_compra.append(Carta(Cor(j), i))
                if i != 5:
                    baralho_compra.append(Carta(Cor(j), i))
        self.getArea_compra().set_baralho_de_cartas(random.sample(baralho_compra, len(baralho_compra)))
        self.distribuiCartasProsJogadores()
        
    def distribuiCartasProsJogadores(self):
        for jogador in self.__jogadores:
            jogador.set_mao_de_cartas(Baralho())
            baralho_jogador = jogador.get_mao_de_cartas().get_baralho_de_cartas()
            for i in range (5):                
                baralho_jogador.append(self.__area_compra.get_baralho_de_cartas()[i])
                self.__area_compra.get_baralho_de_cartas().pop(i)
                
    def descartarCarta(self, carta : Carta):
        self.__area_descarte.get_baralho_de_cartas().append(carta)
        for jogador in self.__jogadores:
            for cartaJogador in jogador.get_mao_de_cartas().get_baralho_de_cartas():
                if cartaJogador == carta:
                    jogador.get_mao_de_cartas().get_baralho_de_cartas().remove(carta)
                    
    def encerrarTurnoJogador(self):
        jogador = self.getJogadorAtual()
        jogador.setSeuTurno(False)
                
    def jogarCarta(self, carta : Carta):
        jogador = self.getJogadorAtual()
        jogador.get_mao_de_cartas().get_baralho_de_cartas().remove(carta)
        self.__area_cartas_jogadas.get_baralho_de_cartas().append(carta)
        
    def getJogadorAtual(self):
        for jogador in self.__jogadores:
            if jogador.getSeuTurno():
                return Jogador
        
    def comprarCarta(self):
        jogador = self.getJogadorAtual()
        cartaComprada = self.__area_compra
        self.__area_compra.get_baralho_de_cartas().remove(cartaComprada)
        jogador.get_mao_de_cartas().get__baralho_de_cartas().append(cartaComprada)
        
    def avaliarFimDeJogo(self):
        #TODO implementar avaliação de fim de jogo
        #TODO retornar booleano
        return
        
            
            
            
            
                    
            
        
        
    
        