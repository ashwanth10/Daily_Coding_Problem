"""
Given a string, return whether it represents a number. Here are the different kinds of numbers:

"10", a positive integer
"-10", a negative integer
"10.1", a positive real number
"-10.1", a negative real number
"1e5", a number in scientific notation
And here are examples of non-numbers:

"a"
"x 1"
"a -2"
"-"
"""
import re

def main():
    i = raw_input("Enter the number?\n")
    pat = re.compile('^[+-]?\d*\.?\d+([eE][-+]?\d+)?$')
    result = pat.match(i)
    result = True if result else False
    print("Valid: {}".format(result))

if __name__ == '__main__':
    main()