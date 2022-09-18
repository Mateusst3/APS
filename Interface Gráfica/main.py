# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 20:20:10 2022

@author: LUCAS
"""

import tkinter as tk
from tkinter import ttk
import random


def showCardInHand(player, card, whichCard=None):
    if card.owner == player.number:
        photo = tk.PhotoImage(file='./back.png')
    else:
        photo = tk.PhotoImage(file='./{}{}.png'.format(card.number, card.color))
    thisCard = ttk.Label(
        player.handFrame,
        image=photo,
        padding=15,
        compound='bottom',
        text='{}'.format(card.number) if card.hasNumberHint is True else '',
        style='{}Card.TLabel'.format(card.color if card.hasColorHint is True else 'back'),
        borderwidth=25,
        relief='sunken'
    )
    # print('{}Card.TLabel'.format(card.color if card.hasColorHint is True else 'back'))
    thisCard.image = photo
    thisCard.pack(side='left', fill='both')
    thisCard.pack_propagate(0)

    # photo = tk.PhotoImage(file='./3red.png')
    # self.playerOneCard1 = ttk.Label(
    #     self.playerOne,
    #     image=photo,
    #     padding=5,
    #     compound='bottom',
    #     text='3',
    #     style='RedCard.TLabel'
    # )
    # self.playerOneCard1.image = photo
    # self.playerOneCard1.pack(side='left', fill='both')


class Player():
    def __init__(self, number, handFrame):
        self.number = number
        self.handFrame = handFrame


class Card():
    def __init__(self, color, number, owner):
        self.color = color
        self.number = number
        self.owner = owner
        self.hasColorHint = False
        self.hasNumberHint = False

    def getColorHint(self):
        self.hasColorHint = True

    def getNumberHint(self):
        self.hasNumberHint = True


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        oneGreen = tk.PhotoImage(file='./Cards/1Green.png')
        oneWhite = tk.PhotoImage(file='./Cards/1White.png')
        twoBlue = tk.PhotoImage(file='./Cards/2Blue.png')
        threeColorful = tk.PhotoImage(file='./Cards/3Colorful.png')
        fourYewllow = tk.PhotoImage(file='./Cards/4Yellow.png')
        fiveRed = tk.PhotoImage(file='./Cards/5Red.png')
        numberCards = [oneGreen, oneWhite, twoBlue, threeColorful, fourYewllow, fiveRed]

        # self.geometry("960x720")
        # self.resizable(False, False)
        self.title('Hanabi')
        # self.iconbitmap('path/to/icon.ico')

        # heading style
        self.style = ttk.Style(self)
        self.style.configure('Heading.TLabel', font=('Helvetica', 12))

        self.style.configure('backCard.TLabel',
                             font=('Helvetica', 12),
                             foreground='black',
                             background='#F2F2F2'
                             )

        self.style.configure('redCard.TLabel',
                             font=('Helvetica', 12),
                             foreground='red',
                             background='#3F0502'
                             )

        self.style.configure('blueCard.TLabel',
                             font=('Helvetica', 12),
                             foreground='blue',
                             background='#02053F'
                             )

        # UI options
        paddings = {'padx': 5, 'pady': 5}
        entry_font = {'font': ('Helvetica', 11)}

        # Configure players hub

        playerHandHeight = 135
        playerHandWidth = 400

        self.playersHub = tk.Frame(self, width=250, bg="#ababab")
        self.playersHubMenu = tk.Frame(self.playersHub, width=playerHandWidth, height=200, bg='black')
        self.playerOneCanvas = tk.Canvas(self.playersHub, width=playerHandWidth, height=200)
        self.playerOne = tk.LabelFrame(self.playerOneCanvas, text="Player one", width=playerHandWidth,
                                       height=playerHandHeight, bg="red")
        self.playerTwo = tk.LabelFrame(self.playersHub, text="Player 2", width=playerHandWidth, height=playerHandHeight,
                                       bg="green")
        self.playerThree = tk.LabelFrame(self.playersHub, text="player three", width=playerHandWidth,
                                         height=playerHandHeight, bg="yellow")
        self.playerFour = tk.LabelFrame(self.playersHub, text="Player 4", width=playerHandWidth,
                                        height=playerHandHeight, bg="white")

        self.playersHubTitle = tk.Label(self.playersHubMenu, text='Players Hub')
        self.playersHubTitle.pack()

        self.playersHubMenu.pack(side='top', fill='both', expand=True)
        self.playerOneCanvas.pack(side='top', fill='both', expand=True)
        self.playerOne.pack(side='top', fill='both', expand=True)
        self.playerTwo.pack(side='top', fill='both', expand=True)
        self.playerThree.pack(side='top', fill='both', expand=True)
        self.playerFour.pack(side='top', fill='both', expand=True)
        # self.playerOne.pack_propagate(0)
        # self.playerTwo.pack_propagate(0)
        # self.playerThree.pack_propagate(0)
        # self.playerFour.pack_propagate(0)
        # self.playerFive.pack_propagate(0)

        # def showCardInHand(player, card, whichCard):
        #     if card.owner == player.number:
        #         photo = tk.PhotoImage(file='./back.png')
        #     else:
        #         photo = tk.PhotoImage(file='./{}{}.png'.format(card.number,card.color))
        #     thisCard = ttk.Label(
        #     player.handFrame,
        #     image=photo,
        #     padding=5,
        #     compound='bottom',
        #     text='{}'.format(card.number) if card.hasNumberHint is True else '',
        #     style='{}Card.TLabel'.format(card.color if card.hasColorHint is True else 'back')
        # )
        #     thisCard.image = photo
        #     thisCard.pack(side='left', fill='both')

        cards = [Card('red', '3', 1) for i in range(5)]
        playerOneObj = Player(1, self.playerTwo)

        for cardIndex, card in enumerate(cards):
            if cardIndex % 2 != 0:
                card.getNumberHint()
            if cardIndex % 3 == 0:
                card.getColorHint()
            showCardInHand(playerOneObj, card)

        # photo = tk.PhotoImage(file='./3red.png')
        def randomCard():
            retorno = numberCards[random.randint(0, len(cards) - 1)]
            return retorno

        self.selectCard = tk.LabelFrame(self, text='Selected Card', bg='#D0E0E0')
        self.selectCard.grid(row=2, column=1, rowspan=1, columnspan=2, sticky="nsew")

        cardOne = randomCard()

        def clickPlayerOneCard1():
            self.teste = ttk.Label(
                self.selectCard,
                image=cardOne,
                padding=5,
                compound='bottom',
                text='3',
                style='RedCard.TLabel'
            )
            self.teste.image = cardOne
            self.teste.pack(side='left', fill='both')

        self.playerOneCard1 = ttk.Button(
            self.playerOne,
            image=cardOne,
            padding=5,
            compound='bottom',
            text='3',
            style='RedCard.TLabel',
            command=clickPlayerOneCard1
        )
        self.playerOneCard1.image = cardOne
        self.playerOneCard1.pack(side='left', fill='both')

        card2 = randomCard()

        def clickPlayerOneCard2():
            self.teste = ttk.Label(
                self.selectCard,
                image=card2,
                padding=5,
                compound='bottom',
                text='3',
                style='RedCard.TLabel'
            )
            self.teste.image = cardOne
            self.teste.pack(side='left', fill='both')

        self.playerOneCard2 = ttk.Button(
            self.playerOne,
            image=card2,
            padding=5,
            compound='bottom',
            text='3',
            style='RedCard.TLabel',
            command=clickPlayerOneCard2
        )
        self.playerOneCard2.image = card2
        self.playerOneCard2.pack(side='left', fill='both')

        card3 = randomCard()

        def clickPlayerOneCard3():
            self.teste = ttk.Label(
                self.selectCard,
                image=card3,
                padding=5,
                compound='bottom',
                text='3',
                style='RedCard.TLabel'
            )
            self.teste.image = card3
            self.teste.pack(side='left', fill='both')

        self.playerOneCard3 = ttk.Button(
            self.playerOne,
            image=card3,
            padding=5,
            compound='bottom',
            text='3',
            style='RedCard.TLabel',
            command=clickPlayerOneCard3
        )
        self.playerOneCard3.image = card3
        self.playerOneCard3.pack(side='left', fill='both')

        card4 = randomCard()

        def clickPlayerOneCard4():
            self.teste = ttk.Label(
                self.selectCard,
                image=card4,
                padding=5,
                compound='bottom',
                text='3',
                style='RedCard.TLabel'
            )
            self.teste.image = card4
            self.teste.pack(side='left', fill='both')

        self.playerOneCard4 = ttk.Button(
            self.playerOne,
            image=card4,
            padding=5,
            compound='bottom',
            text='3',
            style='RedCard.TLabel',
            command=clickPlayerOneCard4
        )
        self.playerOneCard4.image = card4
        self.playerOneCard4.pack(side='left', fill='both')

        card5 = randomCard()

        def clickPlayerOneCard4():
            self.teste = ttk.Label(
                self.selectCard,
                image=card5,
                padding=5,
                compound='bottom',
                text='3',
                style='RedCard.TLabel'
            )
            self.teste.image = card4
            self.teste.pack(side='left', fill='both')

        self.playerOneCard5 = ttk.Button(
            self.playerOne,
            image=card5,
            padding=5,
            compound='bottom',
            text='3',
            style='RedCard.TLabel',
            command=clickPlayerOneCard4
        )
        self.playerOneCard5.image = card5
        self.playerOneCard5.pack(side='left', fill='both')

        cardOnePThree = randomCard()
        self.playerThreeCard1 = ttk.Label(
            self.playerThree,
            image=cardOnePThree,
            padding=5,
            compound='bottom',
            text='3',
            style='RedCard.TLabel'
        )
        self.playerThreeCard1.image = cardOnePThree
        self.playerThreeCard1.pack(side='left', fill='both')

        card2PThree = randomCard()
        self.playerThreeCard2 = ttk.Label(
            self.playerThree,
            image=card2,
            padding=5,
            compound='bottom',
            text='3',
            style='blueCard.TLabel'
        )
        self.playerThreeCard2.image = card2PThree
        self.playerThreeCard2.pack(side='left', fill='both')

        card3PThree = randomCard()
        self.playerThreeCard3 = ttk.Label(
            self.playerThree,
            image=card3PThree,
            padding=5,
            compound='bottom',
            text='3',
            style='RedCard.TLabel'
        )
        self.playerThreeCard3.image = card3PThree
        self.playerThreeCard3.pack(side='left', fill='both')

        card4PThree = randomCard()
        self.playerThreeCard4 = ttk.Label(
            self.playerThree,
            image=card4PThree,
            padding=5,
            compound='bottom',
            text='3',
            style='RedCard.TLabel'
        )
        self.playerThreeCard4.image = card4PThree
        self.playerThreeCard4.pack(side='left', fill='both')

        card5PThree = randomCard()
        self.playerThreeCard5 = ttk.Label(
            self.playerThree,
            image=card5PThree,
            padding=5,
            compound='bottom',
            text='3',
            style='RedCard.TLabel'
        )
        self.playerThreeCard5.image = card5PThree
        self.playerThreeCard5.pack(side='left', fill='both')

        cardOnePFour = randomCard()
        self.playerFourCard1 = ttk.Label(
            self.playerFour,
            image=cardOnePFour,
            padding=5,
            compound='bottom',
            text='3',
            style='RedCard.TLabel'
        )
        self.playerFourCard1.image = cardOnePFour
        self.playerFourCard1.pack(side='left', fill='both')

        card2PFour = randomCard()
        self.playerFourCard2 = ttk.Label(
            self.playerFour,
            image=card2PFour,
            padding=5,
            compound='bottom',
            text='3',
            style='blueCard.TLabel'
        )
        self.playerFourCard2.image = card2PFour
        self.playerFourCard2.pack(side='left', fill='both')

        card3PFour = randomCard()
        self.playerFourCard3 = ttk.Label(
            self.playerFour,
            image=card3PFour,
            padding=5,
            compound='bottom',
            text='3',
            style='RedCard.TLabel'
        )
        self.playerFourCard3.image = card3PFour
        self.playerFourCard3.pack(side='left', fill='both')

        card4PFour = randomCard()
        self.playerFourCard4 = ttk.Label(
            self.playerFour,
            image=card4PFour,
            padding=5,
            compound='bottom',
            text='3',
            style='RedCard.TLabel'
        )
        self.playerFourCard4.image = card4PFour
        self.playerFourCard4.pack(side='left', fill='both')

        card5PFour = randomCard()
        self.playerFourCard5 = ttk.Label(
            self.playerFour,
            image=card5PFour,
            padding=5,
            compound='bottom',
            text='3',
            style='RedCard.TLabel'
        )
        self.playerFourCard5.image = card5PFour
        self.playerFourCard5.pack(side='left', fill='both')

        self.playersHub.grid(row=0, column=0, rowspan=3, columnspan=1, sticky="nsew")

        # self.rowconfigure(1, weight=2)

        # Configure table environment
        # self.playArea = tk.Frame(self, width=15, bg='#206140')
        # self.playAreaTitle = tk.Label(self.playArea, width=5, height=1, text='Play area')
        # self.playAreaTitle.pack(side='top')#, expand=True)
        # self.playArea.grid(row=0, column=1, rowspan=1, columnspan=2, sticky="nsew")

        self.tablePosition = tk.LabelFrame(self, text='Cards played', bg='#D0E0E0')
        self.tablePosition.grid(row=0, column=1, rowspan=1, columnspan=2, sticky="nsew")

        self.playAreaRed = tk.Frame(self.tablePosition, width=72, height=96, bg='#FF3030')
        self.playAreaRed.pack(side='left')
        self.playAreaBlue = tk.Frame(self.tablePosition, width=72, height=96, bg='#3030FF')
        self.playAreaBlue.pack(side='left')
        self.playAreaGreen = tk.Frame(self.tablePosition, width=72, height=96, bg='#30FF30')
        self.playAreaGreen.pack(side='left')
        self.playAreaYellow = tk.Frame(self.tablePosition, width=72, height=96, bg='#F9D71C')
        self.playAreaYellow.pack(side='left')
        self.playAreaWhite = tk.Frame(self.tablePosition, width=72, height=96, bg='#FFFFFF')
        self.playAreaWhite.pack(side='left')

        self.hintArea = tk.Frame(self, bg='#402010')
        self.hintAreaTitle = tk.Label(self.hintArea, text='Number of hints')
        self.hintAreaTitle.pack(side='top', expand=True)
        self.hintArea.grid(row=1, column=1, columnspan=1, sticky='nsew')

        discardText = '1 1 1 2 2 3 3 4 4 5'
        discardTextFormat = '{} {} {} {} {} {} {} {} {} {}'  # .format(range(10))

        self.discardArea = tk.Frame(self, width=200, bg='#4020F0')
        self.discardAreaTitle = tk.Label(self.discardArea, text='Discarded cards')
        self.discardAreaTitle.pack(side='top', expand=True)
        self.discardAreaContentRed = ttk.Label(self.discardArea, text=discardText, style='RedCard.TLabel')
        self.discardAreaContentBlue = ttk.Label(self.discardArea, text=discardText, style='BlueCard.TLabel')
        self.discardArea.grid(row=1, column=2, columnspan=1, sticky='nsew')
        self.discardAreaContentRed.pack(side='top', expand=True)
        self.discardAreaContentBlue.pack(side='top', expand=True)

        # Log of hints
        self.hintLog = tk.Frame(self, width=200, bg='#607040')

        # self.selecionatedCard = tk.Frame(self, width=400)
        # self.selecionatedCardTitle = tk.Label(self.selecionatedCard, text='Selecionated Card')
        # self.selecionatedCardTitle.pack(side='top', expand=True)
        # self.selecionatedCard.grid(row=2, column=1, columnspan=1, sticky='nsew')


# # Create the text widget
# text_widget = tk.Text(master, height=5, width=40)

# # Create a scrollbar
# scroll_bar = tk.Scrollbar(master)

# # Pack the scroll bar
# # Place it to the right side, using tk.RIGHT
# scroll_bar.pack(side=tk.RIGHT)

# # Pack it into our tkinter application
# # Place the text widget to the left side
# text_widget.pack(side=tk.LEFT)

# long_text = """This is a multiline string.
# We can write this in multiple lines too!
# Hello from AskPython. This is the third line.
# This is the fourth line. Although the length of the text is longer than
# the width, we can use tkinter's scrollbar to solve this problem!
# """

# # Insert text into the text widget
# text_widget.insert(tk.END, long_text)

# self.menu_left_lower = tk.Frame(self.playersHub, width=250, bg="blue")

# self.test = tk.Label(self.menu_left_upper, text="test")
# self.test.pack()

# self.menu_left_upper.pack(side="top", fill="both", expand=True)
# self.menu_left_lower.pack(side="top", fill="both", expand=True)

# # configure the grid
# self.columnconfigure(0, weight=1)
# self.columnconfigure(1, weight=3)
# self.columnconfigure(2, weight=1)

# bg = tk.PhotoImage(file='./bg.png')
# canvas = tk.Canvas(self, width=960, height=720)

# canvas.create_image(0, 0, image=bg, anchor='nw')
# # canvas.grid(fill=both, expand=True)

# bgLabel = ttk.Label(self,
#                    image=bg)
# bgLabel.image = bg
# bgLabel.place(x=0, y=0)

# username = tk.StringVar()
# password = tk.StringVar()

# # heading
# heading = ttk.Label(self, text='Member Login', style='Heading.TLabel')
# heading.grid(column=0, row=0, columnspan=3, pady=5, sticky=tk.N)

# # username
# username_label = ttk.Label(self, text="Username:")
# username_label.grid(column=0, row=1, sticky=tk.W, **paddings)

# username_entry = ttk.Entry(self, textvariable=username, **entry_font)
# username_entry.grid(column=1, row=1, sticky=tk.E, **paddings)

# # password
# password_label = ttk.Label(self, text="Password:")
# password_label.grid(column=0, row=2, sticky=tk.W, **paddings)

# password_entry = ttk.Entry(
#     self, textvariable=password, show="*", **entry_font)
# password_entry.grid(column=1, row=2, sticky=tk.E, **paddings)

# # login button
# login_button = ttk.Button(self, text="Login")
# login_button.grid(column=1, row=3, sticky=tk.E, **paddings)

# # configure style
# self.style = ttk.Style(self)
# self.style.configure('TLabel', font=('Helvetica', 11))
# self.style.configure('TButton', font=('Helvetica', 11))

# photo = tk.PhotoImage(file='./3red.png')
# image_label = ttk.Label(
#     self,
#     image=photo,
#     padding=5,
#     compound='bottom',
#     text='3',
#     style='RedCard.TLabel'
# )

# image_label.image = photo
# image_label.grid(column=0, row=3, sticky=tk.E, **paddings)


if __name__ == "__main__":
    app = App()
    app.mainloop()
