import array as arr
import random
from Enumerations.StatusPartida import StatusPartida
from entities.carta import Carta
from entities.jogador import Jogador
from Enumerations.CorDaCarta import Cor


class InterfaceImage:
    def __init__(self):
        self.__mensagem = ""
        self.__area_cartas_jogadas = []
        self.__area_descarte = []
        self.__area_compra = []
        self.__status = StatusPartida.AGUARDANDO_INICIO.value
        self.__jogadores = []
        self.__ultima_rodada = False
        self.__partida_encerrada = False
        
    def get_partida_encerrada(self):
        return self.__partida_encerrada
        
    def set_mensagem(self, mensagem):
        self.__mensagem = mensagem
        
    def get_mensagem(self): 
        return self.__mensagem
    
    def set_area_cartas_jogadas(self, baralho):
        self.__area_cartas_jogadas = baralho
    
    def get_area_cartas_jogadas(self):
        return self.__area_cartas_jogadas
    
    def set_area_descarte(self, baralho):
        self.__area_descarte = baralho
        
    def get_area_descarte(self):
        return self.__area_descarte
    
    def set_area_compra(self, baralho):
        self.__area_compra = baralho
        
    def get_area_compra(self):
        return self.__area_compra
    
    def set_status(self, status):
        self.__status = status
        
    def get_status(self):
        return self.__status
    
    def set_jogadores(self, jogadores):
        self.__jogadores = jogadores
        
    def get_jogadores(self):
        return self.__jogadores
       
    def constroi_baralho_inicial(self):
        baralho_compra = self.get_area_compra()
        for i in range (1,6): #numero
            for j in range (1,6): #cor
                baralho_compra.append(Carta(Cor(j), i))
                if i == 1:
                    baralho_compra.append(Carta(Cor(j), i))
                if i != 5:
                    baralho_compra.append(Carta(Cor(j), i))
        self.set_area_compra(random.sample(baralho_compra, len(baralho_compra)))
        self.distribui_cartas_pros_jogadores()
        
    def distribui_cartas_pros_jogadores(self):
        for jogador in self.__jogadores:
            baralho_jogador = []
            for i in range (5):                
                baralho_jogador.append(self.__area_compra[i])
                self.__area_compra.pop(i)
            jogador.set_mao_de_cartas(baralho_jogador)
                
    def descartar_carta(self, carta : Carta):
        self.__area_descarte.append(carta)
        jogador = self.get_jogador_atual()
        for cartaJogador in jogador.get_mao_de_cartas():
            if cartaJogador == carta:
                jogador.get_mao_de_cartas().remove(carta)
        self.encerrar_turno_jogador()
                    
    def encerrar_turno_jogador(self):
        jogador = self.get_jogador_atual()
        jogador.set_seu_turno(False)
        if self.__ultima_rodada:
            jogador.set_jogou_ultimo_turno(True)
                
    def jogar_carta(self, carta : Carta):
        jogador = self.get_jogador_atual()
        jogador.get_mao_de_cartas().remove(carta)
        self.__area_cartas_jogadas.append(carta)
        
    def get_jogador_atual(self):
        for jogador in self.__jogadores:
            if jogador.get_seu_turno():
                return Jogador
        
    def comprar_carta(self):
        jogador = self.get_jogador_atual()
        cartaComprada = self.__area_compra
        self.__area_compra.remove(cartaComprada)
        jogador.get_mao_de_cartas().append(cartaComprada)
        
    def avaliarFimDeJogo(self, infracoes_cometidas):
        if len(self.__area_cartas_jogadas) == 25:
            self.define_mensagem_fim_de_jogo()
            self.__partida_encerrada = True           
        elif infracoes_cometidas == 3:
            self.__mensagem = "Vocês perderam! O festival foi um fracasso."
            self.__partida_encerrada = True           
        elif len(self.__area_compra) == 0:
            if self.__ultima_rodada:
                jogaram_ultima_rodada = 0
                for jogador in self.__jogadores:
                    if jogador.get_jogou_ultimo_turno():
                        jogaram_ultima_rodada += 1
                if jogaram_ultima_rodada == len(self._jogadores):
                    self.define_mensagem_fim_de_jogo()
                    self.__partida_encerrada = True                               
            else:
                self.__ultima_rodada = True
        return
    
    def define_mensagem_fim_de_jogo(self):
        pontuacao = len(self.__area_cartas_jogadas)
        if pontuacao <= 5:
            self.__mensagem = "Horrível, vaias da multidão."
        elif 6 <= pontuacao <= 10:
            self.__mensagem = "Medíocre, mal se ouvem aplausos."
        elif 11 <= pontuacao <= 15:
            self.__mensagem = "Honrosa, mas não ficará na memória..."
        elif 16 <= pontuacao <= 20:
            self.__mensagem = "Excelente, encanta a multidão."
        elif 21 <= pontuacao <= 24:
            self.__mensagem = "Extraordinária, ficará na memória."
        elif pontuacao == 25:
            self.__mensagem = "Lendária, adultos e crianças atônitos, estrelas em seus olhos!"
    
    def start_match(self, jogadores, id):
        self.__jogadores = []         
        for i in range(len(jogadores)):
            jogador = Jogador(jogadores[i][0], jogadores[i][1], jogadores[i][2])
            if jogador.get_id() == id:
                jogador.set_eh_local(True)
                if jogador.get_posicao == 1:
                    jogador.set_seu_turno(True)
                    self.set_status(3)    
                else:
                    self.set_status(5)
            self.adicionar_jogador(jogador)
        self.constroi_baralho_inicial()
        self.carrega_imagem_cartas()
            
    def adicionar_jogador(self, jogador):
        self.get_jogadores().append(jogador)
        
    def carrega_imagem_cartas(self):
        for carta in self.__area_cartas_jogadas:
            carta.carrega_imagem_carta(True, False)
            
        for carta in self.__area_descarte:
            carta.carrega_imagem_carta(True, False)
            
        for jogador in self.__jogadores:
            if jogador.get_eh_local():
                for carta in jogador.get_mao_de_cartas():
                    carta.carrega_imagem_carta(False, True)
            else: 
                for carta in jogador.get_mao_de_cartas():
                    carta.carrega_imagem_carta(False, False)
                    
    def avaliar_carta_selecionada(self, carta):
        mensagem = "DAR_DICA"
        for jogador in self.__jogadores:
            if jogador.get_eh_local() and jogador.is_carta_no_baralho(carta):
                mensagem = "SELECIONAR_ESPAÇO"
        return mensagem
                
                    
        
            
            
            
            
                    
            
        
        
    
        