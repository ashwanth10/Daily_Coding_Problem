"""
This problem was asked by Google.

Given a string, return the first recurring character in it, or null if there is no recurring character.

For example, given the string "acbbac", return "b". Given the string "abcdef", return null.
"""

def main():
    string = raw_input('enter string?\n')
    s = set()

    for c in string:
        if c in s:
            print(c)
            return
        else:
            s.add(c)
    print('null')

if __name__ == '__main__':
    main()