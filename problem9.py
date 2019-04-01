"""
Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.

Follow-up: Can you do this in O(N) time and constant space?
"""

def main():
    integers = map(int, raw_input("enter the numbers?\n").split())

    excl = 0
    incl = 0

    for number in integers:
        new_excl = max(incl, excl)
        incl = excl + number
        excl = new_excl

    print(max(incl, excl))

if __name__ == '__main__':
    main()