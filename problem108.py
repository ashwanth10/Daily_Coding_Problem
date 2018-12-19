"""
Given two strings A and B, return whether or not A can be shifted some number of times to get B.

For example, if A is abcde and B is cdeab, return true. If A is abc and B is acb, return false.
"""

def main():
    a, b = raw_input("Enter A & B\n").split()

    if len(a) != len(b):
        print(False)

    length_of_a = len(a)
    i = 0

    while(i < length_of_a):
        temp = a[i:length_of_a] + a[:i]
        if temp == b:
            print(True)
            return
        i += 1

    print(False)

if __name__ == '__main__':
    main()