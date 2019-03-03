"""
You are given an array of nonnegative integers.
Let's say you start at the beginning of the array and are trying to advance to the end.
You can advance at most, the number of steps that you're currently on.
Determine whether you can get to the end of the array.

For example, given the array [1, 3, 1, 2, 0, 1], we can go from indices 0 -> 1 -> 3 -> 5, so return true.

Given the array [1, 2, 1, 0, 0], we can't reach the end, so return false.
"""

def get_max_index(lis):
    max_item = 0
    max_index = 0
    for index, item in enumerate(lis):
        if item > max_item:
            max_item = item
            max_index = index
    return max_index

def main():
    elements = map(int, raw_input('enter elements?\n').split())
    length = len(elements)
    index = 0
    while(True and index < length):
        advance_by = elements[index]
        if advance_by > 1:
            advance_by = get_max_index(elements[index + 1: index + advance_by + 1 ]) + 1
        if advance_by == 0:
            break
        index = index + advance_by
    print(True if advance_by else False)


if __name__ == '__main__':
    main()

