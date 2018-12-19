"""
Given an unsigned 8-bit integer, swap its even and odd bits.
The 1st and 2nd bit should be swapped, the 3rd and 4th bit should be swapped, and so on.

For example, 10101010 should be 01010101. 11100010 should be 11010001.

Bonus: Can you do this in one line?
"""

def main():
    given_s = raw_input("Enter an unsigned 8-bit integer?\n")
    print(''.join(map(lambda x, y: y+x, given_s[0:8:2], given_s[1:8:2])))

if __name__ == '__main__':
    main()