"""
This problem was asked by Amazon.

Given n numbers, find the greatest common denominator between them.

For example, given the numbers [42, 56, 14], return 14.
"""

def gcd(a, b):
    remainder = a % b
    if remainder == 0:
        return b
    else:
        a = b
        b = remainder
        return gcd(a, b)


def main():
    numbers = map(int, raw_input('enter numbers?\n').split())
    answer = []
    while(len(numbers) != 1):
        for index in range(len(numbers)-1):
            gcd_value = gcd(numbers[index], numbers[index + 1])
            if gcd_value not in answer:
                answer.append(gcd_value)
        numbers = list(answer)
        answer = []
    print(numbers[0])

if __name__ == '__main__':
    main()