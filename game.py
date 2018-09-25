from player import RandomPlayer, MemoryPlayer
from table import Table

class Game:
    """Game class owning table and players"""
    
    def __init__(self):
        self.table = Table(100)
        self.players = [RandomPlayer(self.table, "Player one"), RandomPlayer(self.table, "Player two")]
        self.counter = 0

    def run(self):
        input()
        while any(self.table.cards):
            for p in self.players:
                if any(self.table.cards):
                    while p.play():
                        if not any(self.table.cards):
                            break
                    common_items = list(set(self.table.cards).intersection(p.captured_cards))
                    if common_items:
                        print(common_items)
                        input()
                else:
                    break

            print("Round: " + str(self.counter))
            self.counter += 1

        print("Game ended")
        if len(self.players[0].captured_cards) > len(self.players[1].captured_cards):
            print("Players 1 won .... " + str(len(self.players[0].captured_cards)) + "cards")
        else: 
            print("Players 2 won .... " + str(len(self.players[1].captured_cards)) + "cards")

        input()
        return