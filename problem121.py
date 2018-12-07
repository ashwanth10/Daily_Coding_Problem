"""
Given a string which we can delete at most k, return whether you can make a palindrome.
For example, given 'waterrfetawx' and a k of 2, you could delete f and x to get 'waterretaw'.
"""

def isPalindrome(s):
    if "".join(reversed(s)) == s: # or s[::-1]
        return True
    return False

def remove_index(s, i, j=None):
    s =  s[:i] + s[i+1:j] + s[j+1:] if j else s[:i] + s[i+1:]
    return s

def main():
    s = raw_input("Enter string?\n")
    k = int(raw_input("Enter 'k'?\n"))
    temp_k = 0
    to_be_removed = []
    i = 0
    j = len(s) - 1
    while(i <= j):
        if s[i] == s[j]:
            i += 1
            j -= 1
            temp_k = 0
        else:
            if temp_k < k:
                to_be_removed.append(s[j])
                temp_k = temp_k + 1
                j = j - 1
            else:
                j += temp_k
                while(temp_k > 0):
                    if to_be_removed:
                        to_be_removed.pop()
                    temp_k -= 1
                to_be_removed.append(s[i])
                i += 1
                temp_k = 0

    for elem in to_be_removed:
        s = s.replace(elem, '')

    if isPalindrome(s) and k >= len(to_be_removed):
        print('Answer: {}'.format(s))
        print('Elements to be removed: {}'.format(to_be_removed))
    else:
        print('cannot be a palindrome with removing {} characters'.format(k))


if __name__ == '__main__':
    main()