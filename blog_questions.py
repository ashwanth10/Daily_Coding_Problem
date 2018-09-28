"""
Solved most of the problems in this blog:
URL: https://hackernoon.com/50-data-structure-and-algorithms-interview-questions-for-programmers-b4b1ac61f5b0
"""

### array problems

def swap(a, b):
    """
    :param a: number
    :param b: number
    :return: b and a
    """
    a = a + b
    b = a - b
    a = a - b
    return (a,b)

def find_missing(lis):
    """
    :param lis: list of numbers
    :return: missing number in the list
    """
    s = sum(lis)
    l = len(lis)
    sl = (l * (l+1)) /2
    m = s - sl
    return(m)

def find_duplicate(lis):
    """
    :param lis: list of numbers
    :return: the duplicate number
    """
    lis.sort()
    for i in range(len(lis)):
        if(lis[i] == lis[i+1]):
            return lis[i]

def smallest_and_largest(lis):
    """
    :param lis: list of numbers
    :return: the smallest and largest
    """
    lis.sort()
    if lis:
        front = lis[0]
        last = lis.pop()
        return(front, last)

def find_pair(lis, k):
    """
    :param lis: list of numbers
    :param k: sum of a pair
    :return: all pairs whose sum is k
    """
    pairs = []
    d = {}
    for item in lis:
        if d.has_key(item):
            pairs.append((item, d[item]))
        else:
            d[k-item] = item
    return(pairs)

def remove_duplicates(lis):
    """
    :param lis: a list of numbers
    :return: a list without any duplicates
    """
    last = -1
    arr = []
    lis.sort()
    for i in range(len(lis)):
        if lis[i] == last:
            continue
        else:
            last = lis[i]
            arr.append(lis[i])
    return(arr)

### String problems

def duplicate_from_string(s):
    """
    :param s: string
    :return: all duplicate characters
    """
    l = []
    a = ''.join(sorted(s))
    for i in range(len(s)):
        if s[i] == s[i+1]:
            l.append(s[i])
    return l

def check_anagrams(x, y):
    """
    :param x: string
    :param y: string
    :return: if x and y are anagrams or not
    """
    x = ''.join(sorted(x))
    y = ''.join(sorted(y))
    return True if x == y else False

def first_non_repeated(s):
    """
    :param s: string
    :return: returns the first non repeated character in that string
    """
    l = []
    d = {}
    for i in range(len(s)):
        if s[i] in l:
            d[s[i]] = False
        else:
            l.append(s[i])
            d[s[i]] = True
    for item in l:
        if d[item]:
            return(item)

def only_digits(s):
    """
    :param s: string
    :return: if it only digits or not
    """
    return s.isdigit()

def vowels_and_consonents(s):
    """
    :param s: a string
    :return: count of vowels and consonants
    """
    vl = ['a', 'e', 'i', 'o', 'u']
    vc = 0
    cc = 0
    for i in range(len(s)):
        if s[i] in vl:
            vc += 1
        else:
            cc += 1
    return(vc,cc)

def permutations_of_string(s):
    """
    :param s: string
    :return: permutations of the string
    """
    from itertools import permutations
    permList = permutations(s)
    return(permList)

def reverse_word_in_string(s):
    """
    :param s: string
    :return: return a string where all words in it are reversed
    """
    s = s.split(' ')
    r_s = []
    for item in s:
        r_s.append(reverse_a_string(item))
    rs = " ".join(r_s)
    return(rs)

def reverse_a_string(s):
    """
    :param s: string
    :return: reversed string
    """
    return s[::-1]

def is_str_palindrome(s):
    """
    :param s: string
    :return: if string is palindrome or not
    """
    l = len(s)
    for i in range(l/2 + 1):
        if s[i] == s[l-i-1]:
            continue
        else:
            return(False)
    return(True)