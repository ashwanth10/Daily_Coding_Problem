"""
Given a word W and a string S, find all starting indices in S which are anagrams of W.

For example, given that W is "ab", and S is "abxaba", return 0, 3, and 4.
"""

def sort_word(word):
    word = ''.join(sorted(word))
    return word

def break_string(string, length):
    list_of_words = []

    for index, item in enumerate(string):
        if(index+length <= len(string)):
            end_index = index + length
            temp_string = string[index:end_index]
            list_of_words.append(temp_string)
        else:
            break

    return(list_of_words)

def main():
    word = raw_input("Enter word?\n").lower()
    string = raw_input("Enter string?\n").lower()
    word = sort_word(word)

    list = break_string(string, len(word))
    answer = []

    for index, item in enumerate(list):
        if sort_word(item) == word:
            answer.append(index)

    print(' '.join(answer))

if __name__ == '__main__':
    main()