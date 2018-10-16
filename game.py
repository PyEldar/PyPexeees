"""A Game class which creates players and runs game loop"""
from pymongo import MongoClient

from player import RandomPlayer, MemoryPlayer
from table import Table

class Game:
    """Game class owning table and players"""

    def __init__(self, table_size=100):
        self.table_size = table_size
        self.table = Table(table_size)
        self.players = [
            MemoryPlayer(20, self.table, "Player one"),
            ]
        # number of rounds - all players played
        self.counter = 1
        self.mongodb = MongoClient().pexes.winners


    def run(self, store_results=False, print_results=False):
        """Runs game loop as long as there are any cards on table"""
        while any(self.table.cards):
            for p in self.players:
                if any(self.table.cards):
                    while p.play():
                        if not any(self.table.cards):
                            break
                else:
                    break
            self.counter += 1

        if print_results:
            for winner in self.get_winners():
                print("{name} won with {count} cards, in round {round}".format(
                    name=winner.name,
                    count=len(winner.captured_cards),
                    round=self.counter,
                    ))

        results = {"rounds": self.counter,
                   "mem_size": self.get_winners()[0].memory.size,
                  }

        if store_results:
            self.store_results(results)

        return results


    def get_winners(self):
        """Return list with players who own most cards"""
        winners = list()
        playres = sorted(self.players, key=lambda p: len(p.captured_cards), reverse=True)
        for player in playres:
            if len(player.captured_cards) == len(playres[0].captured_cards):
                winners.append(player)
        return winners


    def store_results(self, results):
        """Inserts dict to mongo"""
        self.mongodb.insert_one(results)
        print("Storing", results)


    def loop_run(self, num_of_games=50, start_mem_size=1, samples_per_mem_size=10):
        """Runs specified number of games - used for creating statistics"""
        mem_size = start_mem_size
        for i in range(num_of_games):
            total_rounds = 0
            for j in range(samples_per_mem_size):
                self.table = Table(self.table_size)
                self.counter = 1
                self.players = [MemoryPlayer(mem_size, self.table, "Player " + str(i) + str(j))]
                total_rounds += self.run()["rounds"]

            self.store_results({"rounds": total_rounds/samples_per_mem_size, "mem_size": mem_size, "table_size": self.table_size})
            mem_size += 1
