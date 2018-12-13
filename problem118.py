"""
Given a sorted list of integers, square the elements and give the output in sorted order.

For example, given [-9, -2, 0, 2, 3], return [0, 4, 4, 9, 81].
"""

def main():
    sorted_list = map(int, raw_input("Enter the list of numbers by increasing order?\n").split())
    sorted_square_list = map(lambda x: x * x, sorted_list)
    sorted_square_list.sort()
    print(sorted_square_list)

if __name__ == '__main__':
    main()