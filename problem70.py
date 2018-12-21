"""
A number is considered perfect if its digits sum up to exactly 10.
Given a positive integer n, return the n-th perfect number.
For example, given 1, you should return 19. Given 2, you should return 28.
"""

def calc_sum_digits(n):
    total = 0
    while(n > 0):
        total += n % 10
        n = n / 10
    return(total)

def main():
    n = int(raw_input("Enter n?\n"))
    answer = 19
    while(n > 1):
        answer += 9
        if calc_sum_digits(answer) == 10:
            n -= 1
    print(answer)

if __name__ == '__main__':
    main()