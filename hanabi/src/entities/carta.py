import tkinter as tk
import random

from Enumerations.TipoDeDica import TipoDeDica
from Enumerations.CorDaCarta import Cor

class Carta:

    def __init__(self, cor, numero):
        self.__recebeu_dica_cor = False
        self.__cor = cor
        self.__numero = numero
        self.__recebeu_dica_numero = False
        self.__url = ""

    def get_cor(self):
        return self.__cor

    def self_cor(self, cor: Cor):
        self.__cor = cor

    def get_numero(self):
        return self.__numero

    def set_numero(self, numero: int):
        self.__numero = numero

    def get_recebeu_dica_de_cor(self):
        return self.__recebeu_dica_cor

    def set_recebeu_dica_de_cor(self, recebeu_dica_cor__recebeu_dica_cor: bool):
        self.__recebeu_dica_cor = recebeu_dica_cor__recebeu_dica_cor

    def get_recebeu_dica_de_numero(self):
        return self.__recebeu_dica_numero

    def set_recebeu_dica_de_numero(self, recebeu_dica_numero: bool):
        self.__recebeu_dica_numero = recebeu_dica_numero

    def get_url(self):
        return self.__url
    
    def set_url(self, url):
        self.__url = url
    
    def receberDica(self, tipoDeDica : TipoDeDica):
        if tipoDeDica == TipoDeDica.COR:
            self.__recebeu_dica_cor = True
        else: 
            self.__recebeu_dica_numero = True
            
    def carrega_imagem_carta(self, carta_esta_aberta, carta_eh_do_jogador_local):
        url = "src/images/"
        if carta_eh_do_jogador_local:
            url = url + "card"
            if self.__recebeu_dica_cor:
                    url = url + self.__cor.name
            if self.__recebeu_dica_numero: 
                    url = url + str(self.__numero)
        else:
            url = url + self.__cor.name + str(self.__numero)
            if not carta_esta_aberta:
                if self.__recebeu_dica_cor:
                    url = url + "C"
                if self.__recebeu_dica_numero: 
                    url = url + "N"         
        url = url + ".png"
        self.set_url(url)
        