"""
Implement an LRU (Least Recently Used) cache. It should be able to be initialized with a cache size n, and contain the following methods:

set(key, value): sets key to value. If there are already n items in the cache and we are adding a new item, then it should also remove the least recently used item.
get(key): gets the value at key. If no such key exists, return null.
Each operation should run in O(1) time.
"""

import collections

class LRUCache(object):
    def __init__(self, n):
        self._cache_size = n
        self._cache = collections.OrderedDict()

    def set(self, key, value):
        try:
            self._cache.pop(key)
        except KeyError:
            if len(self._cache) >= self._cache_size:
                self._cache.popitem(last=False)
        self._cache[key] = value

    def get(self, key):
        try:
            value = self._cache.pop(key)
            self._cache[key] = value
            return value
        except KeyError:
            return(None)

def main():
    c = LRUCache(10)
    c.set("a", 1)
    print(c.get("a"))

if __name__ == "__main__":
    main()