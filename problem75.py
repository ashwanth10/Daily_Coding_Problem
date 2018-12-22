"""
Given an array of numbers, find the length of the longest increasing subsequence in the array.
The subsequence does not necessarily have to be contiguous.

For example, given the array [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15],
the longest increasing subsequence has length 6: it is 0, 2, 6, 9, 11, 15.
"""

def main():
    lis = map(int, raw_input("Enter the list?\n").split())
    longest_increasing_subsequence = []
    temp_list = []

    for index, item in enumerate(lis):
        if not temp_list:
            temp_list.append(item)
            continue

        if item > temp_list[-1]:
            temp_list.append(item)
        elif(item < temp_list[-1] or (index == len(lis) - 1)):
            if len(temp_list) > len(longest_increasing_subsequence):
                longest_increasing_subsequence = temp_list
            temp_list = [item]

    print(longest_increasing_subsequence)



if __name__ == '__main__':
    main()