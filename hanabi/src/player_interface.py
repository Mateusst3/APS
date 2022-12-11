from tkinter import *
from tkinter import messagebox, ttk
from tkinter import simpledialog, font
from PIL import ImageTk, Image
from dog.dog_interface import DogPlayerInterface
from dog.dog_actor import DogActor
from entities.mesa import Mesa
from Enumerations.StatusPartida import StatusPartida
from Enumerations.CorDaCarta import Cor
from Enumerations.TipoDeDica import TipoDeDica
from entities.carta import Carta


class PlayerInterface(DogPlayerInterface):
    def __init__(self):
        self.main_window = Tk()  # instanciar Tk
        self.board = Mesa()
        self.dog_server_interface = DogActor()
        self.fill_main_window()  # organização e preenchimento da janela
        game_state = self.board.get_estado()
        self.update_gui(game_state)
        player_name = simpledialog.askstring(title="Player identification", prompt="Qual o seu nome?")
        
        message = self.dog_server_interface.initialize(player_name, self)
        messagebox.showinfo(message=message)
        self.opcao_escolhida = None
        self.main_window.mainloop()  # abrir a janela0

    def fill_main_window(self):
        self.main_window.title("Hanabi")
        self.main_window.geometry("1280x720")
        #self.main_window.resizable(False, False)
        
        self.discard_pile = Frame(self.main_window, width=200, height=300)
        self.played_cards = Frame(self.main_window, width=500, height=200)
        self.baralho_de_compras = Frame(self.main_window, width=200, height=200)
        self.dicas_e_infracoes = Frame(self.main_window, width=200, height=200)

        self.discard_pile.grid(row=1, column=1)
        self.played_cards.grid(row=1, column=0)
        self.baralho_de_compras.grid(row=0, column=1)
        self.dicas_e_infracoes.grid(row=2, column=1)

        print(self.main_window.grid_size())

        # self.table_frame = Frame(self.main_window, padx=100, pady=40, bg="gold3")
        # self.table_frame.grid(row=0, column=0)
        # self.message_frame = Frame(self.main_window, padx=0, pady=10)
        # self.message_frame.grid(row=1, column=0)

        self.menubar = Menu(self.main_window)
        self.menubar.option_add("*tearOff", FALSE)
        self.main_window["menu"] = self.menubar

        self.menu_file = Menu(self.menubar)
        self.menubar.add_cascade(menu=self.menu_file, label="File")

        self.menu_file.add_command(label="Iniciar jogo", command=self.start_match)
        self.menu_file.add_command(label="Restaurar estado inicial", command=self.start_game)

    def start_match(self):
        match_status = self.board.get_estado().get_status()
        if match_status == 1:
            answer = messagebox.askyesno("START", "Deseja iniciar uma nova partida?")
            if answer:
                start_status = self.dog_server_interface.start_match(2)
                code = start_status.get_code()
                message = start_status.get_message()
                if code == "0" or code == "1":
                    messagebox.showinfo(message=message)
                else:  # (code=='2')
                    players = start_status.get_players()
                    local_player_id = start_status.get_local_id()
                    self.board.start_match(players, local_player_id)
                    game_state = self.board.get_estado()
                    self.update_gui(game_state)
                    messagebox.showinfo(message=start_status.get_message())

    def receive_start(self, start_status):
        self.start_game()  # use case reset game
        players = start_status.get_players()
        local_player_id = start_status.get_local_id()
        self.board.start_match(players, local_player_id)
        game_state = self.board.get_estado()
        self.update_gui(game_state)

    def start_game(self):
        match_status = self.board.get_estado().get_status()
        if match_status == 2 or match_status == 6:
            self.board.reset_game()
            game_state = self.board.get_estado()
            self.update_gui(game_state)

    def receive_withdrawal_notification(self):
        self.board.receber_notificacao_desistencia()
        game_state = self.board.get_estado()
        self.update_gui(game_state)
        messagebox.showinfo(message = "O jogador desistiu. Partida encerrada!")
        

    def update_gui(self, game_state):
        self.update_menu_status()
        jogadores = game_state.get_jogadores()

        self.mostrar_cartas_descartadas(game_state)
        self.mostrar_cartas_jogadas(game_state)
        self.mostra_baralho_compra(game_state)
        self.mostra_dicas_e_infracoes(game_state)
        self.mostra_baralho_jogadores(jogadores)
        
    def mostra_baralho_jogadores(self, jogadores):
        self.local_player_hand = Frame(self.main_window, width=550, height=300)
        self.remote_player_hand = Frame(self.main_window, width=550, height=300)
        
        self.remote_player_hand.grid(row=0, column=0)       
        self.local_player_hand.grid(row=2, column=0)
        
        for jogador in jogadores:
            if jogador.get_eh_local():
                for i in range(len(jogador.get_mao_de_cartas())):
                    carta = jogador.get_mao_de_cartas()[i]
                    img = ImageTk.PhotoImage(Image.open(carta.get_url()).resize((125, 200)))
                    cartaM = ttk.Button(
                        self.local_player_hand,
                        image=img,
                        padding=5,
                        compound='bottom',
                        command = lambda carta = carta : self.selecionar_carta(carta)
                    )
                    cartaM.image = img
                    cartaM.pack(side='left', fill='both')  

            else:
                for i in range(len(jogador.get_mao_de_cartas())):
                    carta = jogador.get_mao_de_cartas()[i]
                    img = ImageTk.PhotoImage(Image.open(carta.get_url()).resize((125, 200)))
                    cartaM = ttk.Button(
                        self.remote_player_hand,
                        image=img,
                        padding=5,
                        compound='bottom',
                        command = lambda carta = carta : self.selecionar_carta(carta)
                    )
                    cartaM.image = img
                    cartaM.pack(side='left', fill='both')

    def mostrar_cartas_descartadas(self, game_state):

        cartas_descartadas = game_state.get_area_descarte()

        titulo_cartas_descartadas = Label(self.discard_pile,
                                          text='Cartas descartadas',
                                          font=font.Font(size=12, weight='bold'))
        titulo_cartas_descartadas.grid(row=0, column=0)

        textos = ['' for i in range(5)]

        for carta in cartas_descartadas:
            cor_atual = carta.get_cor().value - 1 # Enum inicia no índice 1
            textos[cor_atual] += str(carta.get_numero())

        for texto, cor in zip(textos, Cor):
            texto = list(texto)
            texto.sort()
            texto = ' '.join(texto)
            linha = Label(self.discard_pile, text=texto, fg=cor.name, font=font.Font(size=12,))
            linha.grid(row=cor.value, column=0)

    def mostrar_cartas_jogadas(self, game_state):
        
        self.played_cards = Frame(self.main_window, width=100, height=200)
        self.played_cards.grid(row=1, column=0)
        
        cartas_jogadas = game_state.get_area_cartas_jogadas()

        # cartas_jogadas = [Carta(Cor.red, 2),
        #                       Carta(Cor.blue, 5),
        #                       Carta(Cor.white, 2),
        #                       Carta(Cor.blue, 2),
        #                       Carta(Cor.blue, 2),
        #                       Carta(Cor.blue, 2),
        #                       ]

        #self.board.get_estado().set_area_cartas_jogadas(cartas_jogadas)
        
        cartas_mais_altas = [0 for i in range(5)]

        for cor in Cor:
            carta_mais_alta = self.board.get_numero_carta_mais_alta_da_cor(cor)
            if carta_mais_alta:
                carta = Carta(cor, carta_mais_alta)
                carta.carrega_imagem_carta(True, False)
                cartas_mais_altas[cor.value-1] = carta

        for carta in cartas_mais_altas:
            if carta:
                img = ImageTk.PhotoImage(Image.open(carta.get_url()).resize((125, 200)))
            else:
                img = ImageTk.PhotoImage(Image.open("src/images/cardjogada.png").resize((125, 200)))
            cartaM = ttk.Button(
                self.played_cards,
                image=img,
                padding=5,
                compound='bottom'
            )
            cartaM.image = img
            # cartaM.disable()
            cartaM.pack(side='left', fill='both')

    def mostra_baralho_compra(self, game_state):
        self.baralho_de_compras = Frame(self.main_window, width=200, height=200)
        self.baralho_de_compras.grid(row=0, column=1)
        
        img = ImageTk.PhotoImage(Image.open("src/images/card.png").resize((125, 200)))
        cartaB = ttk.Button(
            self.baralho_de_compras,
            image=img,
            padding=25,
            compound='bottom',
            style='RedCard.TLabel',
            text=str(len(game_state.get_area_compra())),
        )
        cartaB.image = img
        cartaB.pack(side='left', fill='both')

    def mostra_dicas_e_infracoes(self, game_state):
        numero_total_de_dicas = 8
        self.dicas_e_infracoes = Frame(self.main_window, width=200, height=200)
        self.dicas_e_infracoes.grid(row=2, column=1)
        
        dicas = Frame(self.dicas_e_infracoes)
        dicas.grid(row=0, column=0)

        infracoes = Frame(self.dicas_e_infracoes,)
        infracoes.grid(row=1, column=0)
        
        dicas_restantes = Label(dicas,
                                text='Dicas disponíveis',
                                fg='black',
                                font=font.Font(size=12,),
                                )
        dicas_usadas = Label(dicas,
                                text='Dicas usadas',
                                fg='black',
                                font=font.Font(size=12,)
                                )
        numero_dicas_restantes = Label(dicas,
                                text=str(game_state.get_dicas_disponiveis()),
                                fg='black',
                                font=font.Font(size=12,)
                                )
        numero_dicas_usadas = Label(dicas,
                                text=str(numero_total_de_dicas-game_state.get_dicas_disponiveis()),
                                fg='black',
                                font=font.Font(size=12,)
                                )

        infracoes_cometidas = Label(infracoes,
                                    text='Infrações cometidas',
                                    font=font.Font(size=12)
                                    )
        numero_infracoes_cometidas = Label(infracoes,
                                    text=str(game_state.get_infracoes_cometidas()),
                                    fg='red',
                                    font=font.Font(size=12, weight='bold')
                                    )
    
        dicas_restantes.grid(row=0, column=0, padx=5)
        dicas_usadas.grid(row=0, column=1, padx=5)
        numero_dicas_restantes.grid(row=1, column=0, padx=5)
        numero_dicas_usadas.grid(row=1, column=1, padx=5)

        infracoes_cometidas.grid(row=0, column=0, columnspan=2)
        numero_infracoes_cometidas.grid(row=1, column=0, columnspan=2)

    def update_menu_status(self):
        match_status = self.board.get_estado().get_status()
        if match_status == 2 or match_status == 6:
            self.menu_file.entryconfigure("Restaurar estado inicial", state="normal")
        else:
            self.menu_file.entryconfigure("Restaurar estado inicial", state="disabled")
        if match_status == 1:
            self.menu_file.entryconfigure("Iniciar jogo", state="normal")
        else:
            self.menu_file.entryconfigure("Iniciar jogo", state="disabled")

    def popup_dar_dica(self, carta):       
        popup = Toplevel()
        popup.geometry("250x250+350+200")
        popup.resizable(False,False)
        popup.title("Escolha uma dica")
        label = Label(popup, text="Escolha uma dica", font=font.Font(size=12, weight='bold'))
        label.pack(side="top", pady=10)
        button1 = Button(popup, text="Voltar", command=popup.destroy)
        button1.pack(side='bottom', pady=10)
        button2 = Button(popup, text="Cor", command = lambda : self.clicar_no_botao_de_dica(popup, carta, TipoDeDica.COR))
        button2.pack(side='bottom', pady=10)
        button3 = Button(popup, text="Número", command= lambda : self.clicar_no_botao_de_dica(popup, carta, TipoDeDica.NUMERO))
        button3.pack(side='bottom', pady=10)

    def clicar_no_botao_de_dica(self, popup, carta, tipoDeDica):
        popup.destroy()
        mensagem = self.board.dar_dica(carta, tipoDeDica)
        if mensagem != "":
            messagebox.showinfo(message=mensagem)
        else:
            game_state = self.board.get_estado()
            self.update_gui(game_state)
            self.dog_server_interface.send_move(game_state)
            
    def popup_jogar_descartar_carta(self, carta):       
        popup = Toplevel()
        popup.geometry("250x250+350+200")
        popup.resizable(False,False)
        popup.title("O que você quer fazer com a carta?")
        label = Label(popup, text="Escolha uma opção:", font=font.Font(size=12, weight='bold'))
        label.pack(side="top", pady=10)
        button1 = Button(popup, text="Voltar", command=popup.destroy)
        button1.pack(side='bottom', pady=10)
        button2 = Button(popup, text="Jogar carta", command = lambda : self.jogar_carta(popup, carta))
        button2.pack(side='bottom', pady=10)
        button3 = Button(popup, text="Descartar carta", command= lambda : self.descartar_carta(popup, carta))
        button3.pack(side='bottom', pady=10)
        
    def jogar_carta(self, popup, carta):
        popup.destroy()
        self.board.jogar_carta(carta)
        game_state = self.board.get_estado()
        self.update_gui(game_state)
        self.dog_server_interface.send_move(game_state)
        
    def descartar_carta(self, popup, carta):
        #DELETAR DEPOIS
        self.board.get_estado().set_dicas_disponiveis(5)
        #--------------------------------------
        popup.destroy()
        mensagem = self.board.descartar_carta(carta)
        if mensagem != "":
            messagebox.showinfo(message=mensagem)
        else:
            game_state = self.board.get_estado()
            self.update_gui(game_state)
            self.dog_server_interface.send_move(game_state)
          

    def selecionar_carta(self, carta):
        if self.board.get_estado().get_status() == 3:        
            mensagem = self.board.selecionar_carta(carta)
            
            if mensagem == "DAR_DICA":
                self.popup_dar_dica(carta)
            else:
                self.popup_jogar_descartar_carta(carta)
        else: 
            messagebox.showinfo(message = "Aguarde seu turno para jogar!")
            
    def receive_move(self, a_move):
        self.board.receber_jogada(a_move)
        game_state = self.board.get_estado()
        self.update_gui(game_state)