import random

class Player:
    """Parent class abstracting players"""
    captured_cards = {}
    
    def __init__(self, table):
        self.table = table

    def play(self):
        """begins move"""
        
        if any(self.table.cards):
            first, second = random.sample(range(0, len(self.table.cards) -1), 2)
            while (self.table.cards[first] is None or self.table.cards[second] is None) and any(self.table.cards):
                first, second = random.sample(range(0, len(self.table.cards) -1), 2)
            
            print("trying")
            print(first, second)
            print("table")
            print(self.table.cards[first])
            print(self.table.cards[second])
            
            #take cards from table
            if (self.table.cards[first] is not None and self.table.cards[second] is not None) and (self.table.cards[first].id == self.table.cards[second].id):
                self.table.cards[first] = None
                self.table.cards[second] = None
                #success - continue move
                print("GOT CARDS")
                self.play()


class RandomPlayer(Player):
    """Player without memory - randomly turns cards"""
    pass


class MemoryPlayer(Player):
    """Player with specified memory size - 0 == infinite"""
    def __init__(self, memory_size):
        pass
