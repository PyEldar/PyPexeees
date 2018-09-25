import copy
from random import shuffle

from card import Card

class Table:
    def __init__(self, size):
        self.size = size
        self.cards = self.assembleCards(size)
    
    def assembleCards(self, size):
        cards = []

        for x in range(size//2):
            card = Card(x)
            clone = copy.deepcopy(card)
            cards.extend((card, clone))

        shuffle(cards)

        for card in cards:
            print(card)

        return cards


