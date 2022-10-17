import random
import tkinter as tk


class Carta:

    def __init__(self, cor, numero):
        self.__recebeuDicaDeCor = None
        self.__cor = cor
        self.__numero = numero
        self.__receuDicaDeNumero = None
        self.__urls = ["./Cards/1Green.png", "Cards/1White", "Cards/2Blue", "Cards/3Colorful", "Cards/4Yellow", "Cards/5Red"]
        # self.__urlDestino = "Cards/" + str(numero) + cor + ".png"
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
        self.__receuDicaDeNumero = recebeuDicaDeNumero

    def get_url(self):
        return self.__urlDestino
