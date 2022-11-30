import random
import tkinter as tk

from InterfaceGrafica.Enumerations.TipoDeDica import TipoDeDica
#TODO implementar metodo que gera a URL das cartas de acordo com: 
    #Se a carta está ou não no baralho do jogador (se sim, sempre começa com card)
    #Se a carta recebeu ou não dica. Se recebeu dica de cor, terá um C no final e se recebeu dica de número, um N. Se recebeu os 2, é CN. (ver nomes das cartas na pasta image)

class Carta:

    def __init__(self, cor, numero):
        self.__recebeuDicaDeCor = False
        self.__cor = cor
        self.__numero = numero
        self.__recebeuDicaDeNumero = False
        self.__url = ""
        self.__urlDestino = tk.PhotoImage(file=self.__urls[0])

    def get_cor(self):
        return self.__cor

    def self_cor(self, cor: str):
        self.__cor = cor

    def get_numero(self):
        return self.__numero

    def set_numero(self, numero: int):
        self.__numero = numero

    def get_recebeu_dica_de_cor(self):
        return self.__recebeuDicaDeCor

    def set_recebeu_dica_de_cor(self, recebeuDicaDeCor: bool):
        self.__recebeuDicaDeCor = recebeuDicaDeCor

    def get_recebeu_dica_de_numero(self):
        return self.__recebeuDicaDeNumero

    def set_recebeu_dica_de_cor(self, recebeuDicaDeNumero: bool):
        self.__recebeuDicaDeNumero = recebeuDicaDeNumero

    def get_url(self):
        return self.__urlDestino

    def carregar_url(self):
        return ""
    
    def receberDica(self, tipoDeDica : TipoDeDica):
        if tipoDeDica == TipoDeDica.COR:
            self.__recebeuDicaDeCor = True
        else: 
            self.__recebeuDicaDeNumero = True
        