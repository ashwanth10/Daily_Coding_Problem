"""
This problem was asked by Facebook.

Given a 32-bit integer, return the number with its bits reversed.

For example, given the binary number 1111 0000 1111 0000 1111 0000 1111 0000, return 0000 1111 0000 1111 0000 1111 0000 1111.
"""


def main():
    bytes = raw_input('Enter the binary number?\n').split()
    invert = lambda x: '0' if int(x) else '1'
    bits_reversed = ''
    for byte in bytes:
        bits_reversed += ''.join(map(invert, byte)) + ' '

    print(bits_reversed)

if __name__ == '__main__':
    main()