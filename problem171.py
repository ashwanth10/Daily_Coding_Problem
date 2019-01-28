"""
You are given a list of data entries that represent entries and exits of groups of people into a building. An entry looks like this:
{"timestamp": 1526579928, count: 3, "type": "enter"}

This means 3 people entered the building. An exit looks like this:
{"timestamp": 1526580382, count: 2, "type": "exit"}

This means that 2 people exited the building. timestamp is in Unix time.
Find the busiest period in the building, that is, the time with the most people in the building.
Return it as a pair of (start, end) timestamps. You can assume the building always starts off and ends up empty, i.e. with 0 people inside.
"""

class DataEntry():
    def __init__(self):
        self._count = 0
        self._data = []

    def add_entry(self, timestamp, count, type):
        if type == "enter":
            self._count += count
        else:
            self._count -= count
        entry = {
            "timestamp" : timestamp,
            "count" : count,
            "type" : type,
            "count_till_now" : self._count
        }
        self._data.append(entry)

    def busy_period(self):
        max_count = max_count_index = 0
        if self._data:
            for index, entry in enumerate(self._data):
                if entry.get('count_till_now') > max_count:
                    max_count_index = index
                    max_count = entry.get('count_till_now')
        busy_period = (self._data[max_count_index].get('timestamp'), self._data[max_count_index + 1].get('timestamp'))
        return busy_period

def main():
    n = int(raw_input("enter no. of entires?\n"))

    d = DataEntry()
    while(n > 0):
        timestamp, count, type = raw_input().split()
        d.add_entry(int(timestamp), int(count), type)
        n -= 1

    print(d.busy_period())


if __name__ == '__main__':
    main()