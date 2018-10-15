from operator import attrgetter

from player import RandomPlayer, MemoryPlayer
from table import Table

class Game:
    """Game class owning table and players"""

    def __init__(self):
        self.table = Table(100)
        self.players = [
            MemoryPlayer(0, self.table, "Player one"),
            MemoryPlayer(0, self.table, "Player two"),
            MemoryPlayer(0, self.table, "Player three"),
            MemoryPlayer(0, self.table, "Player four"),
            MemoryPlayer(0, self.table, "Player fice"),
            MemoryPlayer(0, self.table, "Player six"),
            RandomPlayer(self.table, "Player seven")
            ]
        self.counter = 0

    def run(self):
        """Runs game loop as long as there are any cards on table"""
        input()
        while any(self.table.cards):
            for p in self.players:
                if any(self.table.cards):
                    while p.play():
                        if not any(self.table.cards):
                            break
                else:
                    break

            print("Round: " + str(self.counter))
            self.counter += 1

        print("Game ended")
        winner = max(self.players, key=attrgetter('captured_cards.__len__'))
        print("{name} won with {count} cards".format(
            name=winner.name,
            count=len(winner.captured_cards),
            ))

        input()
        return
