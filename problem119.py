"""
Given a set of closed intervals, find the smallest set of numbers that covers all the intervals.
If there are multiple smallest sets, return any of them.
For example, given the intervals [0, 3], [2, 6], [3, 4], [6, 9], one set of numbers that covers all these intervals is {3, 6}.
"""

def update_list(answer, interval):
    a = interval[0]
    b = interval[1]
    available = False
    for item in range(a, b + 1):
        if item == answer[0] or item == answer[1]:
            available = True
            break
    if not available:
        if answer[1] < a:
            answer[1] = a
        else:
            answer[0] = b
    return answer


def main():
    i = int(raw_input("Enter the number of intervals?\n"))
    max_list = min_list = []
    while i:
        a, b = map(int, raw_input("Enter {} interval\n".format(i)).split(' '))
        if not min_list or not max_list:
            min_list = [a, a]
            max_list = [b, b]
        min_list = update_list(min_list, [a, b])
        max_list = update_list(max_list, [a, b])
        i = i - 1

    len_of_min = min_list[1] - min_list[0]
    len_of_max = max_list[1] - min_list[0]
    print("Answer: {}".format(min_list if len_of_min <= len_of_max else max_list))


if __name__ == "__main__":
    main()