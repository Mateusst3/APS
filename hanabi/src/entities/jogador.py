class Jogador:

    def __init__(self, nome, id, posicao):
        self.__nome = nome
        self.__mao_de_cartas = None
        self.__jogou_ultimo_turno = None
        self.__posicao = posicao
        self.__seu_turno = False
        self.__jogador_id = id
        self.__eh_local = False

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome: str):
        self.__nome = nome

    def get_mao_de_cartas(self):
        return self.__mao_de_cartas
    
    def set_mao_de_cartas(self, baralho):
        self.__mao_de_cartas = baralho

    def get_jogou_ultimo_turno(self):
        return self.__jogou_ultimo_turno

    def set_jogou_ultimo_turno(self, jogou: bool):
        self.__jogou_ultimo_turno = jogou

    def jogar_descartar_carta(self, carta_jogada):
        for carta in self.__mao_de_cartas:
            if carta == carta_jogada:
                self.__mao_de_cartas.remove(carta)

    def comprar_carta(self, carta):
        self.__mao_de_cartas.append(carta)

    def get_posicao(self):
        return self.__posicao

    def get_seu_turno(self):
        return self.__seu_turno

    def set_seu_turno(self, seu_turno__seu_turno: bool):
        self.__seu_turno = seu_turno__seu_turno
        
    def get_id(self):
        return self.__jogador_id
    
    def set_id(self, id):
        self.__jogador_id = id
        
    def get_eh_local(self):
        return self.__eh_local
    
    def set_eh_local(self, eh_local):
        self.__eh_local = eh_local
        
    def is_carta_no_baralho(self, carta):
        for carta_jogador in self.__mao_de_cartas:
            if carta_jogador == carta:
                return True
        return False
