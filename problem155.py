"""
This problem was asked by MongoDB.
Given a list of elements, find the majority element, which appears more than half the time (> floor(len(lst) / 2.0)).
You can assume that such element exists.
For example, given [1, 2, 1, 1, 3, 4, 0], return 1.
"""

def main():
    lis = map(int, raw_input("Enter list?\n").split())
    lis.sort()
    l = len(lis) / 2

    max_count = 0
    previous_item = lis[0]
    count = 1
    ans = previous_item
    for item in lis[1:]:
        if item == previous_item:
            count += 1
        else:
            if count > max_count:
                max_count = count
                ans = previous_item
            previous_item = item
            count = 1
    print(ans if max_count > l else "")

if __name__ == '__main__':
    main()