"""
Given an even number (greater than 2), return two prime numbers whose sum will be equal to the given number.
A solution will always exist. See Goldbach's conjecture: https://en.wikipedia.org/wiki/Goldbach%27s_conjecture

Input: 4
Output: 2 + 2 = 4
If there are more than one solution possible, return the lexicographically smaller solution.

If [a, b] is one solution with a <= b, and [c, d] is another solution with c <= d, then

[a, b] < [c, d]
If a < c OR a==c AND b < d.
"""



def compute_primes(n):
    i = 2
    primes = []
    while(i < n):
        if n % i == 0:
            primes.append(i)
        i += 1
    return(primes)

def main():
    n = int(raw_input("Enter an even number?\n"))
    primes = compute_primes(n)

    for i in primes:
        pair = n - i
        if pair in primes:
            print(i, pair)
            break

if __name__ == '__main__':
    main()