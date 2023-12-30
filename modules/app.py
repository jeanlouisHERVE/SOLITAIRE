#!/usr/bin/env python
# packages
import random
from classes.card import Card
from classes.deck import Deck
# other modules


# own packages







# Example usage:
deck = Deck()
deck.shuffle()

# Draw and print five cards
for _ in range(5):
    card = deck.draw_card()
    print(card)