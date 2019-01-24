"""
Given a list of words, find all pairs of unique indices such that the concatenation of the two words is a palindrome.

For example, given the list ["code", "edoc", "da", "d"], return [(0, 1), (1, 0), (2, 3)].
"""

def is_palindrome(word):
    return word == word[::-1]

def main():
    words = raw_input("Enter the words?\n").split()
    no_of_words = len(words)
    index_range = range(0, len(words))
    result = []

    for first_index in range(0, no_of_words):
        second_index = range(0, first_index) + range(first_index + 1, no_of_words)

        for index in second_index:
            string = words[first_index] + words[index]
            if is_palindrome(string):
                result.append((first_index, index))

    print(result)

if __name__ == '__main__':
    main()