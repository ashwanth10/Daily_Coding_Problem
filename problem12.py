"""
There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time.
Given N, write a function that returns the number of unique ways you can climb the staircase.
The order of the steps matters.

For example, if N is 4, then there are 5 unique ways:

1, 1, 1, 1
2, 1, 1
1, 2, 1
1, 1, 2
2, 2
What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a set of positive integers X?
For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.
"""

def climbsteps_for_1_or_2(n):
    if n == 1:
        return 1
    elif n == 2:
         return 2
    else:
        return climbsteps_for_1_or_2(n-1) + climbsteps_for_1_or_2(n-2)

def countWaysUtil(n, m):
    res = [0] * n
    res[0] = 1

    for i in range(1, n):
        for j in range(1, i + 1) and m:
            res[i] += res[i-j]

    return res[n-1]

def countWays(s, m):
    return countWaysUtil(s + 1, m)

def main():
    no_of_steps = int(raw_input("enter no. of steps?\n"))
    is_set_given = raw_input("entering set?\n").startswith("y")
    if is_set_given:
        l = map(int, raw_input("enter the steps?\n").split())
        print(countWays(no_of_steps, l))
    else:
        print(climbsteps_for_1_or_2(no_of_steps))


if __name__ == '__main__':
    main()