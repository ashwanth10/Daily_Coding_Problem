"""
This problem was asked by Amazon.

Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.

For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".
"""

def noOfDistinctCharacters(word):
    checker = 0
    noOfDictinct = 0
    for i in range(len(word)):
        bitAtIndex = ord(word[i]) - ord('a')
        if(checker & (1 << bitAtIndex) > 0):
            continue
        checker = checker | (1 << bitAtIndex)
        noOfDictinct += 1
    return noOfDictinct

def main():
    k = int(raw_input("enter integer?\n"))
    s = raw_input("enter string?\n")
    string_dict = {}

    for i in range(len(s)):
        for j in range(i+1, len(s) + 1):
            word = s[i:j]
            count = noOfDistinctCharacters(word)
            if(count > k):
                break
            if (not string_dict.get(count, None)):
                string_dict[count] = [word]
            else:
                string_dict.get(count).append(word)

    for i in range(k, 0, -1):
        if(string_dict.get(i, None)):
            temp_list = string_dict.get(i)
            temp_list.sort(key=lambda x: len(x), reverse=True)
            print(temp_list[0])
            break


if __name__ == '__main__':
    main()