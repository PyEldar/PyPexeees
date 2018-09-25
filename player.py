import random
from collections import OrderedDict

class Player:
    """Parent class abstracting players"""
    
    def __init__(self, table, name):
        self.table = table
        self.name = name
        self.captured_cards = []

    def play(self):
        """begins move"""
        raise NotImplementedError("Must be implemented in subclass")

    def __str__(self):
        return self.name


class RandomPlayer(Player):
    """Player without memory - randomly turns cards"""

    def play(self):
        """Make move 

        returns True on success
        """

        first, second = random.sample(range(0, len(self.table.cards)), 2)
        while (self.table.cards[first] is None or self.table.cards[second] is None) and any(self.table.cards):
            first, second = random.sample(range(0, len(self.table.cards)), 2)

        #take cards from table
        if self.table.cards[first].id == self.table.cards[second].id:
            self.captured_cards.append(self.table.cards[first].id)
            self.table.cards[first] = None
            self.table.cards[second] = None

            return True

        return False


class MemoryPlayer(Player):
    """Player with specified memory size - 0 == infinite"""
    def __init__(self, memory_size, *args, **kwargs):
        super(MemoryPlayer, self).__init__(*args, **kwargs)
        self.memory_size = memory_size
        self.memory = OrderedDict()

    def play(self):
        """Make move
        when first item is in memory use stored value to get the right card
        """
        #get first card which is not already taken or is not in your memory
        first = random.randint(0, len(self.table.cards) -1)
        second = None
        while (first in self.memory.keys() or self.table.cards[first] is None) and any(self.table.cards):
            first = random.randint(0, len(self.table.cards) -1)

        #check memory if there is not info about currently turned card
        for key, value in self.memory.items():
            print("memory check")
            if self.table.cards[first] == value:
                second = key
                break

        if not second:
            second = random.randint(0, len(self.table.cards) -1)
            while self.table.cards[second] is None and any(self.table.cards):
                second = random.randint(0, len(self.table.cards) -1)
        
        #take cards from table
        if self.table.cards[first].id == self.table.cards[second].id:
            self.captured_cards.append(self.table.cards[first].id)
            self.table.cards[first] = None
            self.table.cards[second] = None

            return True

        return False