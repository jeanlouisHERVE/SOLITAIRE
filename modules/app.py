#!/usr/bin/env python
# packages
import random

# other modules


# own packages

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank} of {self.suit}"


class Deck:
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


# Example usage:
deck = Deck()
deck.shuffle()

# Draw and print five cards
for _ in range(5):
    card = deck.draw_card()
    print(card)