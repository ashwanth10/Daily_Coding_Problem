"""
You have 100 fair coins and you flip them all at the same time.
Any that come up tails you set aside. The ones that come up heads you flip again.
How many rounds do you expect to play before only one coin remains?

Write a function that, given n, returns the number of rounds you'd expect to play until one coin remains.
"""

def main():
    n = float(raw_input("Enter the no. of coins?\n"))
    chances = 0

    while(n > 1):
        n = n / 2.0
        chances += 1

    print(chances)

if __name__ == '__main__':
    main()