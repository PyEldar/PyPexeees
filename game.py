from player import Player
from table import Table

class Game:
    """Game class owning table and players"""
    
    def __init__(self):
        self.table = Table(10)
        self.players = [Player(self.table), Player(self.table)]
        self.counter = 0

    def run(self):
        while True:
            if any(self.table.cards):
                [p.play() for p in self.players]
                print("Round: " + str(self.counter))
                self.counter += 1

            else:
                print("Game ended")
                if len(self.players[0].captured_cards) > len(self.players[1].captured_cards):
                    print("Players 1 won .... " + str(len(self.players[0].captured_cards)) + "cards")
                else: 
                    print("Players 2 won .... " + str(len(self.players[1].captured_cards)) + "cards")
                return