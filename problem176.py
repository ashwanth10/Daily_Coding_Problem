"""
This problem was asked by Bloomberg.
Determine whether there exists a one-to-one character mapping from one string s1 to another s2.
For example, given s1 = abc and s2 = bcd, return true since we can map a to b, b to c, and c to d.
Given s1 = foo and s2 = bar, return false since the o cannot map to two characters.
"""

def check_one_to_one(string1, string2):
    map = {}
    one_to_one = True

    for index, character in enumerate(string1):
        if map.get(character, None):
            if string2[index] == map.get(character):
                continue
            else:
                one_to_one = False
                break
        else:
            map[character] = string2[index]
    return one_to_one

def main():
    string1 = list(raw_input('enter string1?\n'))
    string2 = list(raw_input('enter string2?\n'))
    print(check_one_to_one(string1, string2))

if __name__ == '__main__':
    main()