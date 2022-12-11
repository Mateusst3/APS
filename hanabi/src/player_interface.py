from tkinter import *
from tkinter import messagebox, ttk
from tkinter import simpledialog, font
from PIL import ImageTk, Image
from dog.dog_interface import DogPlayerInterface
from dog.dog_actor import DogActor
from entities.mesa import Mesa
from Enumerations.StatusPartida import StatusPartida
from Enumerations.CorDaCarta import Cor
from entities.carta import Carta


class PlayerInterface(DogPlayerInterface):
    def __init__(self):
        self.main_window = Tk()  # instanciar Tk
        self.board = Mesa()
        self.fill_main_window()  # organização e preenchimento da janela
        game_state = self.board.get_estado()
        self.update_gui(game_state)
        player_name = simpledialog.askstring(title="Player identification", prompt="Qual o seu nome?")
        self.dog_server_interface = DogActor()
        message = self.dog_server_interface.initialize(player_name, self)
        messagebox.showinfo(message=message)
        self.main_window.mainloop()  # abrir a janela0

    def fill_main_window(self):
        self.main_window.title("Hanabi")
        self.main_window.geometry("1280x720")
        #self.main_window.resizable(False, False)
        
        self.discard_pile = Frame(self.main_window, width=200, height=300, bg='gray')
        self.played_cards = Frame(self.main_window, width=100, height=30, bg='green')
        self.local_player_hand = Frame(self.main_window, width=550, height=300, bg="gold3")
        self.remote_player_hand = Frame(self.main_window, width=550, height=300, bg="red")
        self.baralho_de_compras = Frame(self.main_window, width=400, height=400, bg='black')
        self.dicas_remanescentes = Frame(self.main_window, width=400, height=400, bg='blue')

        self.remote_player_hand.grid(row=0, column=0)
        self.discard_pile.grid(row=1, column=1)
        self.played_cards.grid(row=1, column=0)
        self.local_player_hand.grid(row=2, column=0)
        self.baralho_de_compras.grid(row=0, column=1)
        self.dicas_remanescentes.grid(row=2, column=1)

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
                start_status = self.dog_server_interface.start_match(1)
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
        self.board.get_estado().set_status(StatusPartida.DESISTENCIA.value)
        game_state = self.board.get_estado()
        self.update_gui(game_state)

    def update_gui(self, game_state):
        self.update_menu_status()
        jogadores = game_state.get_jogadores()

        self.mostrar_cartas_descartadas(game_state)
        self.mostrar_cartas_jogadas(game_state)
        self.mostra_baralho(game_state)

        for jogador in jogadores:
            if jogador.get_eh_local():
                for carta in jogador.get_mao_de_cartas():
                    # carta.set_url("src/images/blue1.png")
                    img = ImageTk.PhotoImage(Image.open(carta.get_url()).resize((125, 200)))
                    cartaM = ttk.Button(
                        self.local_player_hand,
                        image=img,
                        padding=5,
                        compound='bottom',
                        style='RedCard.TLabel',
                    )
                    cartaM.image = img
                    cartaM.pack(side='left', fill='both')

            else:
                for carta in jogador.get_mao_de_cartas():
                    img = ImageTk.PhotoImage(Image.open(carta.get_url()).resize((125, 200)))
                    cartaM = ttk.Button(
                        self.remote_player_hand,
                        image=img,
                        padding=5,
                        compound='bottom',
                        style='RedCard.TLabel',
                    )
                    cartaM.image = img
                    cartaM.pack(side='left', fill='both')

    def mostrar_cartas_descartadas(self, game_state):
        cartas_descartadas = game_state.get_area_descarte()

        # DELETAR {
        cartas_descartadas = [Carta(Cor.red, 2),
                              Carta(Cor.blue, 5),
                              Carta(Cor.blue, 2),
                              Carta(Cor.blue, 2),
                              ]
        # DELETAR }

        textos = ['' for i in range(5)]

        for carta in cartas_descartadas:
            cor_atual = carta.get_cor().value - 1 # Enum inicia no índice 1
            textos[cor_atual] += str(carta.get_numero())

        for texto, cor in zip(textos, Cor):
            texto = list(texto)
            texto.sort()
            texto = ' '.join(texto)
            linha = Label(self.discard_pile, text=texto, fg=cor.name, font=font.Font(size=12,))
            linha.grid(row=cor.value-1, column=0)

    def mostrar_cartas_jogadas(self, game_state):
        
        self.played_cards = Frame(self.main_window, width=100, height=30, bg='green')
        self.played_cards.grid(row=1, column=0)
        
        cartas_jogadas = game_state.get_area_cartas_jogadas()

        cartas_jogadas = [Carta(Cor.red, 2),
                              Carta(Cor.blue, 5),
                              Carta(Cor.white, 2),
                              Carta(Cor.green, 2),
                              ]
        # DELETAR }
        
        
        cartas_mais_altas = [0 for i in range(5)]

        for indice_cor in range(5):
            carta_mais_alta = self.board.get_numero_carta_mais_alta_da_cor(indice_cor + 1)
            if carta_mais_alta:
                cartas_mais_altas[indice_cor] = Carta(indice_cor + 1, carta_mais_alta)

        # DELETAR 
        #cartas_mais_altas = cartas_jogadas

        print(cartas_mais_altas)
        for carta in cartas_mais_altas:
            if carta:
                img = ImageTk.PhotoImage(Image.open(carta.get_url()).resize((125, 200)))
                cartaM = ttk.Button(
                    self.played_cards,
                    image=img,
                    padding=5,
                    compound='bottom',
                    style='RedCard.TLabel',
                )
                cartaM.image = img
                cartaM.pack(side='left', fill='both')
            else:
                img = ImageTk.PhotoImage(Image.open("src/images/card.png").resize((125, 200)))
                cartaM = ttk.Button(
                    self.played_cards,
                    image=img,
                    padding=5,
                    compound='bottom',
                    style='RedCard.TLabel',
                )
                cartaM.image = img
                cartaM.pack(side='left', fill='both')

    def mostra_baralho(self, game_state):
        self.baralho_de_compras = Frame(self.main_window, width=200, height=250, bg='black')
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

    def mostra_dicas(self, game_state):
        self.dicas_remanescentes = Frame(self.main_window, width=400, height=400, bg='blue')
        self.dicas_remancescentes.grid(row=2, column=1)
        
        dicas_restantes = Label(self.dicas_remanescentes,
                                text='Dicas disponíveis',
                                fg='black',
                                font=font.Font(size=12,)
                                )
        dicas_usadas = Label(self.dicas_remanescentes,
                                text='Dicas usadas',
                                fg='black',
                                font=font.Font(size=12,)
                                )
        numero_dicas_restantes = Label(self.dicas_remanescentes,
                                text=str(),
                                fg='black',
                                font=font.Font(size=12,)
                                )
        numero_dicas_usadas = Label(self.dicas_remanescentes,
                                text=str(),
                                fg='black',
                                font=font.Font(size=12,)
                                )
    
        dicas_restantes.grid(row=0, column=0)
        dicas_usadas.grid(row=0, column=1)
        numero_dicas_restantes.grid(row=1, column=0)
        numero_dicas_usadas.grid(row=1, column=1)

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

    def selecionar_carta(self, event, carta):
        mensagem = self.board.selecionar_carta(carta)
        if mensagem == "DAR_DICA":
            # TODO implementar fluxo dar dica:
            # Mostrar popup na tela com duas opcoes: dica de numero ou dica de cor
            # O tipo de dica é o que vier dessa entrada
            tipo_de_dica = ''  # TipoDeDica.Cor OU TipoDeDica.Numero
            mensagem = self.board.dar_dica(carta, tipo_de_dica)
            if mensagem != "":
                return
                # TODO Mostrar pop-up na tela com a mensagem recebida
            else:
                game_state = self.board.get_estado()
                self.update_gui(game_state)
        else:
            # TODO implementar fluxo selecionar ou descartar carta:
            # Mostrar popup na tela com duas opcoes: descartar a carta ou jogar a carta
            # A opcao selecionada é a escolhida pelo jogador na tela
            opcao_selecionada = ''
            if opcao_selecionada == "JOGAR_CARTA":
                self.board.jogar_carta(carta)
                self.board.receber_jogada()
                game_state = self.board.get_estado()
                self.update_gui(game_state)
            else:
                mensagem = self.board.descartar_carta(carta)
                if mensagem != "":
                    # TODO Mostrar pop-up na tela com a mensagem recebida
                    return
                else:
                    game_state = self.board.get_estado()
                    self.update_gui(game_state)
