"""
Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.
For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].
Follow-up: what if you can't use division?
"""

def main():
    arr = raw_input('list of numbers\n')
    arr = map(lambda x: int(x), arr.split())

    n = len(arr)
    left = [0] * n
    right = [0] * n
    left[0] = 1
    right[n-1] = 1

    for i in range(1, n):
        left[i] = arr[i-1] * left[i-1]

    for i in range(n-2,-1, -1):
        right[i] = arr[i+1] * right[i+1]

    ans = map(lambda x,y: x*y, left,right)
    print(ans)

if __name__ == '__main__':
    main()

