"""
Given a string, determine whether any permutation of it is a palindrome.
For example, carrace should return true, since it can be rearranged to form racecar, which is a palindrome.
daily should return false, since there's no rearrangement that can form a palindrome.
"""

def main():
    string = raw_input("enter string?\n")
    count_dict = {}
    for c in string:
        if count_dict.get(c, None):
            count_dict[c] = count_dict[c] + 1
        else:
            count_dict[c] = 1

    valid_once = False

    for count in count_dict.values():
        if count % 2 == 1:
            if valid_once:
                print('False')
                return
            valid_once = True

    print('True')



if __name__ == '__main__':
    main()