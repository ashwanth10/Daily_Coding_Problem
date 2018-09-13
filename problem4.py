"""
Given an array of integers, find the first missing positive integer in linear time and constant space.
In other words, find the lowest positive integer that does not exist in the array.
The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.
"""
# TODO: Use better sorting algorithm

def first_missing(nums):
    if not nums:
        return 1
    i = 0
    while(i <= len(nums) - 1):
        if nums[i] != (i+1):
            ans = i + 1
            return ans
        i += 1
    ans = i + 1
    return ans

def sort_nums(nums):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if(nums[i] > nums[j]):
                nums[i], nums[j] = nums[j], nums[i]
    return nums

def main():
    nums = raw_input("Enter the numbers: ")
    nums = map(int, nums.split(' '))
    nums = sort_nums(nums)
    nums = filter(lambda x: x > 0, nums)
    ans = first_missing(nums)
    print(ans)

if __name__ == "__main__":
    main()