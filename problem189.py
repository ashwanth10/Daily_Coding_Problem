"""
Given an array of elements, return the length of the longest subarray where all its elements are distinct.

For example, given the array [5, 1, 3, 5, 2, 3, 4, 1], return 5 as the longest subarray of distinct elements is [5, 2, 3, 4, 1].
"""

def main():
    array = map(int, raw_input('enter elements?\n').split())
    temp_array = []
    max_length = 0

    for item in array:
        if item not in temp_array:
            temp_array.append(item)
        else:
            if(len(temp_array) > max_length):
                max_length = len(temp_array)
                answer_array = list(temp_array)
            i = temp_array.index(item)
            temp_array = temp_array[i+1: ] + [item]

    answer_array = temp_array if len(temp_array) > max_length else answer_array
    max_length = len(temp_array) if len(temp_array) > max_length else max_length

    print(max_length)
    print(answer_array)


if __name__ == '__main__':
    main()