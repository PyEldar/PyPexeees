"""A Game class which runs game loop"""
from pymongo import MongoClient

from player import RandomPlayer, MemoryPlayer
from table import Table


class Game:
    """Game class containing table and players"""

    def __init__(self, table_size=100):
        self.table_size = table_size
        self.table = Table(table_size)
        self.players = [
            RandomPlayer(self.table, 'Player one random'),
            MemoryPlayer(1, self.table, 'Player two memory'),
            MemoryPlayer(1, self.table, 'Player three memory'),
        ]
        self.counter = 1
        self.mongodb = MongoClient().pexes

    def run(self):
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

        results = {
            'players': self.players,
            'winner': self.get_winners(),
            'round': self.counter
        }
        self.show_results()
        return results

    def get_winners(self):
        """Return list with players who own most cards"""
        winners = list()
        playres = sorted(self.players, key=lambda p: len(p.captured_cards), reverse=True)
        for player in playres:
            if len(player.captured_cards) == len(playres[0].captured_cards):
                winners.append(player)
        return winners

    def show_results(self):
        for winner in self.get_winners():
            print("{name} won with {count} cards, in round {round}".format(
                name=winner.name,
                count=len(winner.captured_cards),
                round=self.counter,
                ))

    def store_results(self, results):
        """Inserts dict to mongo"""
        self.mongodb.comparisions.insert_one(results)

    def loop_run(self, num_of_games=50, start_mem_size=0, samples_per_mem_size=10):
        """Runs specified number of games - used for creating statistics"""
        mem_size = start_mem_size
        for i in range(num_of_games):
            cards = [0, 0]
            for j in range(samples_per_mem_size):
                self.table = Table(self.table_size)
                self.counter = 1
                self.players = [
                    RandomPlayer(self.table, 'Player Random {}{}'.format(i, j)),
                    MemoryPlayer(mem_size, self.table, 'Player Memory {}{}'.format(i, j))
                ]

                results = self.run()
                cards[0] += len(results['players'][0].captured_cards)
                cards[1] += len(results['players'][1].captured_cards)

            cards[0] = cards[0] / samples_per_mem_size
            cards[1] = cards[1] / samples_per_mem_size

            self.store_results({'random_player': cards[0], 'memory_player': cards[1], "mem_size": mem_size})
            mem_size += 1
