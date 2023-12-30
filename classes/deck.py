#!/usr/bin/env python
import random

class Deck:
    
    from card import Card

    def __init__(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

        self.cards = [Card(suit, rank) for suit in suits for rank in ranks]

    def shuffle(self):
        random.shuffle(self.cards)

    def draw_card(self):
        if not self.is_empty():
            return self.cards.pop()
        else:
            print("The deck is empty.")

    def is_empty(self):
        return len(self.cards) == 0