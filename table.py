import copy
from random import shuffle

from card import Card


class Table:
    """Represents table with pairs of cards"""
    def __init__(self, size):
        self.size = size
        self.cards = self.assemble_cards(size)

    def assemble_cards(self, size):
        """Creates list with card pairs, size means total size of final list"""
        cards = []
        for x in range(size//2):
            card = Card(x)
            clone = copy.deepcopy(card)
            cards.extend((card, clone))

        shuffle(cards)
        return cards
