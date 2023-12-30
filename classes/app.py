#!/usr/bin/env python
# packages
from deck import Deck
# other modules


# own packages


# Example usage:
deck = Deck()
deck.shuffle()

# Draw and print five cards
# for _ in range(5):
#     card = deck.draw_card()
#     print(card)

result = deck.print_all_cards()
print("result", result)
