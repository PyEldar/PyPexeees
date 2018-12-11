import random

from memory import LimitedMemory


class Player:
    """Parent class abstracting players"""

    def __init__(self, table, name):
        self.table = table
        self.name = name
        self.captured_cards = []

    def play(self):
        """begins move"""
        raise NotImplementedError("Must be implemented in a subclass")

    def __str__(self):
        return self.name


class RandomPlayer(Player):
    """Player without memory - randomly turns cards"""

    def play(self):
        """Make move
        returns True on success
        """
        first, second = self.choose_cards()

        # take cards from table
        if self.table.cards[first].id == self.table.cards[second].id:
            self.captured_cards.append(self.table.cards[first].id)
            self.table.cards[first] = None
            self.table.cards[second] = None

            return True

        return False

    def choose_cards(self):
        first = random.randint(0, len(self.table.cards) - 1)
        while self.table.cards[first] is None and any(self.table.cards):
                first = random.randint(0, len(self.table.cards) - 1)

        second = random.randint(0, len(self.table.cards) - 1)
        while (self.table.cards[second] is None or first == second) and any(self.table.cards):
                second = random.randint(0, len(self.table.cards) - 1)
        return first, second


class MemoryPlayer(Player):
    """Player with specified memory size - 0 == infinite"""
    def __init__(self, memory_size, *args, **kwargs):
        super(MemoryPlayer, self).__init__(*args, **kwargs)
        self.memory = LimitedMemory(memory_size)

    def play(self):
        """Make move
        when first item is in memory use stored value to get the right card
        """
        first, second = self.choose_cards()
        # take cards from table
        if self.table.cards[first].id == self.table.cards[second].id:
            self.captured_cards.append(self.table.cards[first].id)
            self.table.cards[first] = None
            self.table.cards[second] = None

            return True

        self.save_card(first, self.table.cards[first])
        self.save_card(second, self.table.cards[second])

        return False

    def choose_cards(self):
        first, second = self.check_memory()

        # get first card which is not already taken or is not in your memory
        if first is None:
            first = random.randint(0, len(self.table.cards) - 1)
            while (first in self.memory.keys() or self.table.cards[first] is None) and any(self.table.cards):
                first = random.randint(0, len(self.table.cards) - 1)

        if second is None:
            second = self.lookup_card(first)

        if second is None:
            second = random.randint(0, len(self.table.cards) - 1)
            while (self.table.cards[second] is None or first == second) and any(self.table.cards):
                second = random.randint(0, len(self.table.cards) - 1)
        return first, second

    def save_card(self, position, card):
        """saves card to memory if it is not there yet"""
        if card not in self.memory.keys():
            self.memory.set(position, card.id)

    def lookup_card(self, position):
        """check for match in memory, return card index on positive"""
        for key, value in self.memory.items():
            if self.table.cards[position].id == value:
                return key
        return None

    def check_memory(self):
        """checks memory if there are two identical cards returns indexes"""
        for value in self.memory.values():
            keys = self.get_keys_by_value(self.memory, value)
            if len(keys) > 1:
                # check if card is still on table
                if self.table.cards[keys[0]]:
                    # remove keys from memory
                    [self.memory.pop(key) for key in keys]
                    return keys
        return None, None

    def get_keys_by_value(self, source_dict, to_find):
        """Returns keys of *source_dict* with value *to_find*"""
        keys = list()
        for key, value in source_dict.items():
            if value == to_find:
                keys.append(key)
        return keys
