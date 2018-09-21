class Player:
    """Parent class abstracting players"""
    pass


class RandomPlayer(Player):
    """Player without memory - randomly turns cards"""
    pass


class MemoryPlayer(Player):
    """Player with specified memory size - 0 == infinite"""
    def __init__(self, memory_size):
        pass
