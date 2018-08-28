"""
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
Bonus: Can you do this in one pass?
"""

def main():
    n = raw_input("Enter the list of numbers\n")
    n = map(lambda x: int(x), n.split())
    k = int(raw_input("Enter k\n"))
    d = {}
    print(n)
    for i in n:
        a = k - i
        if d.has_key(i):
            return True
        else:
            d[a] = i
    return False

if __name__ == '__main__':
    print(main())