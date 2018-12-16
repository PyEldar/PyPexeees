"""represents memory with specified size"""
from collections import OrderedDict


class LimitedMemory:
    """Class internalluy uses OrderedDict and has dict-like methods

    methods for storing, retrieving - get(key), set(key, value)
    """
    def __init__(self, size=0):
        self.size = size
        self.storage = OrderedDict()

    def set(self, key, value):
        """Stores value under key"""
        self.storage[key] = value
        if len(self.storage) > self.size:
            self.pop(last=False)

    def get(self, key):
        """Returns value by key"""
        return self.storage[key]

    def pop(self, key=None, last=None):
        """Pops last item if not key or last=False is specified"""
        if last is not None:
            return self.storage.popitem(last=last)
        return self.storage.pop(key)

    def items(self):
        """Returns set-like object containing tuples (key, value)"""
        return self.storage.items()

    def values(self):
        """Returns a list-like object containing all values"""
        return self.storage.values()

    def keys(self):
        """Returns a set-like object containing keys"""
        return self.storage.keys()
