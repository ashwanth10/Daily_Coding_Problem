"""
Given an array of positive integers, divide the array into two subsets such that the difference between the sum of the subsets is as small as possible.

For example, given [5, 10, 15, 20, 25], return the sets {10, 25} and {5, 15, 20}, which has a difference of 5, which is the smallest possible difference.
"""

import bisect

def get_diff(a, b):
    return a - b

def main():
    numbers = map(int, raw_input('enter numbers?\n').split())
    set_one = []
    set_two = []
    numbers.sort()
    flag = False

    for item in numbers:
        diff_one = get_diff(sum(set_one) + item, sum(set_two))
        diff_two = get_diff(sum(set_two) + item, sum(set_one))

        if diff_one < diff_two:
            while(set_one and True):
                diff_two = get_diff(sum(set_two) + item, sum(set_one))
                index = bisect.bisect_right(set_two, diff_two) - 1
                if(0 <= index < len(set_two)):
                    set_one.append(set_two.pop(index))
                else:
                    set_two.append(item)
                    flag = True
                    break
            if not flag:
                set_one.append(item)
                flag = False
        else:
            while(set_two and True):
                diff_one = get_diff(sum(set_one) + item, sum(set_two))
                index = bisect.bisect_right(set_one, diff_one) - 1
                if(0 <= index < len(set_one)):
                    set_two.append(set_one.pop(index))
                else:
                    set_one.append(item)
                    flag = True
                    break
            if not flag:
                set_two.append(item)
                flag = False

    print(set_one)
    print(set_two)


if __name__ == '__main__':
    main()