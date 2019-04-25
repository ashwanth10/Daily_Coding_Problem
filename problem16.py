"""
You run an e-commerce website and want to record the last N order ids in a log. Implement a data structure to accomplish this, with the following API:

record(order_id): adds the order_id to the log
get_last(i): gets the ith last element from the log. i is guaranteed to be smaller than or equal to N.
You should be as efficient with time and space as possible.
"""

class ecommerce(object):
    def __init__(self, N):
        self.N = N;
        self._log = []

    def get_last(self, i):
        if len(self._log) > i and i >= 0:
            return self._log[i]
        else:
            return -1

    def record(self, order_id):
        if len(self._log) == self.N:
            self._log.pop()
            self._log.insert(0, order_id)
        else:
            self._log.insert(0, order_id)


def main():
    website = ecommerce(10)
    website.record(100)
    website.record(110)
    website.record(120)
    print(website.get_last(2))

if __name__ == '__main__':
    main()