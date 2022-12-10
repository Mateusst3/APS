from tkinter import *
from tkinter import messagebox, ttk
from tkinter import simpledialog
from PIL import ImageTk, Image
from dog.dog_interface import DogPlayerInterface
from dog.dog_actor import DogActor
from entities.mesa import Mesa
from Enumerations.StatusPartida import StatusPartida


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
        self.main_window.resizable(False, False)

        self.local_player_hand = Frame(self.main_window, width=550, height=300, bg="gold3")
        self.remote_player_hand = Frame(self.main_window, width=550, height=300, bg="red")

        self.local_player_hand.grid(row=1, column=0)
        self.remote_player_hand.grid(row=0, column=0)
        self.local_player_hand.pack()

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
        # local_player_labels = self.generate_local_player_labels()
        # remote_player_labels = self.generate_remote_player_labels()
        local_players_cards_labels = []
        remote_players_cards_labels = []

        for jogador in jogadores:
            if jogador.get_eh_local():
                for carta in jogador.get_mao_de_cartas():
                    carta.set_url("./images/blue1.png")
                    img = ImageTk.PhotoImage(Image.open(carta.get_url()).resize((100, 200)))
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
                    img = ImageTk.PhotoImage(Image.open(carta.get_url()).resize((100, 200)))
                    cartaM = ttk.Button(
                        self.remote_player_hand,
                        image=img,
                        padding=5,
                        compound='bottom',
                        style='RedCard.TLabel',
                    )
                    cartaM.image = img
                    cartaM.pack(side='left', fill='both')

        self.local_player_hand.grid(row=1, column=0)
        self.remote_player_hand.grid(row=0, column=0)
        # for carta in local_players_cards_labels:
        #     carta.pack(side='left', fill='both')

        # TODO implementar pra mostrar a carta dos jogadores
        # o que tentei aqui NÃO FUNCIONAAAAA D:

        # Mostra cartas jogadores

        # for jogador in jogadores:
        #     if jogador.get_eh_local():
        #         for i in range(len(jogador.get_mao_de_cartas())):
        #             img = ImageTk.PhotoImage(Image.open(jogador.get_mao_de_cartas()[i].get_url()))
        #             label = local_player_labels[i]
        #             label.configure(image = img)
        #             label.grid(row = 1, column = i)
        #             if i < 4 and label == local_player_labels[i+1]:
        #                 print(label)
        #     else:
        #         for i in range(len(jogador.get_mao_de_cartas())):
        #             img = ImageTk.PhotoImage(Image.open(jogador.get_mao_de_cartas()[i].get_url()))
        #             label = remote_player_labels[i]
        #             label.configure(image = img)
        #             label.grid(row = 1, column = i)

        # self.local_player_hand.grid(row = 1, column = 0)
        # self.remote_player_hand.grid(row = 0, column = 0)

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
