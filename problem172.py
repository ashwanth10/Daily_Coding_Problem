"""

Given a string s and a list of words words, where each word is the same length, find all starting indices of substrings in s that is a concatenation of every word in words exactly once.

For example, given s = "dogcatcatcodecatdog" and words = ["cat", "dog"], return [0, 13], since "dogcat" starts at index 0 and "catdog" starts at index 13.

Given s = "barfoobazbitbyte" and words = ["dog", "cat"], return [] since there are no substrings composed of "dog" and "cat" in s.

The order of the indices does not matter.
"""

def main():
    string = raw_input("enter the string?\n")
    words = raw_input("enter the words?\n").split()

    if not words and string:
        raise ValueError
        return

    length = len(words[0])
    temp_words = list(words)
    index = 0
    start_index = None
    answer = []

    while(index < len(string)):
        test_word = string[index : index + length]
        if not temp_words:
            answer.append(start_index)
            temp_words = list(words)
            index = start_index + 1
            start_index = None
        elif test_word in temp_words:
            if start_index is None:
                start_index = index
            temp_words.remove(test_word)
            index += length
        else:
            temp_words = list(words)
            if not start_index:
                index += 1
            else:
                index = start_index + 1
            start_index = None

    if not temp_words:
        answer.append(start_index)

    print(answer)


if __name__ == '__main__':
    main()