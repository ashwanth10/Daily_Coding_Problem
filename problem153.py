"""
Find an efficient algorithm to find the smallest distance (measured in number of words) between any two given words in a string.

For example, given words "hello", and "world" and a text content of "dog cat hello cat dog dog hello cat world", return 1 because there's only one word "cat" in between the two words.
"""

def main():
    word1, word2 = raw_input("Enter two words?\n").split()
    text = raw_input("Enter the text?\n")

    text = text.split()
    found_word1 = (False, 0)
    shortest_distance = len(text)

    for index, word in enumerate(text):
        if word == word1:
            found_word1 = (True, index)

        if found_word1[0]:
            if word == word2:
                found_word2 = (True, index)
                distance = found_word2[1] - found_word1[1] - 1
                if distance < shortest_distance:
                    shortest_distance = distance
                found_word1 = (False, None)

    print(shortest_distance)


if __name__ == '__main__':
    main()