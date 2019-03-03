"""
Given a collection of intervals, find the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

Intervals can "touch", such as [0, 1] and [1, 2], but they won't be considered overlapping.

For example, given the intervals (7, 9), (2, 4), (5, 8), return 1 as the last interval can be removed and the first two won't overlap.

The intervals are not necessarily sorted in any order.

Learnt: use classes instead of index
"""

def get_input():
    n = int(raw_input('enter the number of intervals?\n'))
    intervals = []

    while (n > 0):
        interval = map(int, raw_input().split())
        intervals.append(interval)
        n = n - 1

    return sorted(intervals, key= lambda interval: interval[1])

def main():
    intervals = get_input()
    final_intervals = []
    current_time = -1
    for interval in intervals:
        if interval[0] >= current_time:
            final_intervals.append(interval)
            current_time = interval[1]

    print(final_intervals)
    print(len(intervals) - len(final_intervals))



if __name__ == '__main__':
    main()