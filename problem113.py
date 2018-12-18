"""
Given a string of words delimited by spaces, reverse the words in string. For example, given "hello world here", return "here world hello"

Follow-up: given a mutable string representation, can you perform this operation in-place?
"""

def reverse_word(word):
    return word[::-1]

def main():
    given_s = raw_input("Enter the string?")
    given_s = given_s[::-1]
    start_index = 0
    for index, item in enumerate(given_s):
        if item == ' ':
            end_index = index
            temp = reverse_word(given_s[start_index:end_index])
            given_s = given_s[:start_index] + temp + given_s[end_index:]
            start_index = index + 1

    temp = reverse_word(given_s[end_index:])
    given_s = given_s[:end_index+1] + temp
    print(given_s)

if __name__ == '__main__':
    main()