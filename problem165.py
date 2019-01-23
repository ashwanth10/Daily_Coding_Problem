"""
Given an array of integers, return a new array where each element in the new array is the number of smaller elements to the right of that element in the original input array.

For example, given the array [3, 4, 9, 6, 1], return [1, 1, 2, 1, 0], since:

    There is 1 smaller element to the right of 3
    There is 1 smaller element to the right of 4
    There are 2 smaller elements to the right of 9
    There is 1 smaller element to the right of 6
    There are no smaller elements to the right of 1

"""
import bisect

def main():
    lis = map(int, raw_input("enter the elements?\n").split())
    length = len(lis)
    result_list = [0] * length
    index = length - 2
    sorted_list = [lis[-1]]

    for item in lis[::-1][1:]:
        no_of_smaller_elements = bisect.bisect_left(sorted_list, item)
        sorted_list = sorted_list[:no_of_smaller_elements] + [item] + sorted_list[no_of_smaller_elements:]
        result_list[index] = no_of_smaller_elements
        index -= 1

    print(result_list)

if __name__ == '__main__':
    main()