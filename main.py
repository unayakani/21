import random

class Card():
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

class Dealer():
    def __init__(self, card1, card2, card3, card4):
        self.card1 = card1
        self.card2 = card2
        self.card3 = card3
        self.card4 = card4

class Player():
    def __init__(self, card1, card2, card3, card4):
        self.card1 = card1
        self.card2 = card2
        self.card3 = card3
        self.card4 = card4

values = {'Ace':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'Jack':10, 'Queen':10, 'King':10}

suits = ['Ace', 'Clubs', 'Hearts', 'Diamonds']

while True:
    print('Welcome to 21!')
