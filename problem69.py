"""
Given a list of integers, return the largest product that can be made by multiplying any three integers.

For example, if the list is [-10, -10, 5, 2], we should return 500, since that's -10 * -10 * 5.

Three are three approaches:
* Naive approach O(n3) ... loop three times and calculate for each triplet
* O(nlog n) ... sort the array and compute the max(product of last 3 elements , product of first 2 and last)
* O(n) ... iterate over the list. Compute three max's and 2 min's. Then find max( product of 3 maxs, product of 2 min & max)
"""

def main():
    lis = map(int, raw_input("Enter list?\n").split())
    first_max = second_max = third_max = first_min = second_min = 0
    for elem in lis:
        if elem > first_max:
            third_max = second_max
            second_max = first_max
            first_max = elem
        elif elem > second_max:
            third_max = second_max
            second_max = elem
        elif elem > third_max:
            third_max = elem
        elif elem < first_min:
            second_min = first_min
            first_min = elem
        elif elem < second_min:
            second_min = elem

    print(max(first_max * second_max * third_max , first_min * second_min * first_max))


if __name__ == '__main__':
    main()