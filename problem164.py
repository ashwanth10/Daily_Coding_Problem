"""
You are given an array of length n + 1 whose elements belong to the set {1, 2, ..., n}.
By the pigeonhole principle, there must be a duplicate. Find it in linear time and space.
"""

def main():
    lis = map(int, raw_input("enter list?\n").split())
    length = len(lis)
    space = [0] * (length - 1)
    for item in lis:
        if space[item-1] == 0:
            space[item-1] = item
        else:
            print('duplicate is: {}'.format(item))


if __name__ == '__main__':
    main()