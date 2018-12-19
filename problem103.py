"""
Given a string and a set of characters, return the shortest substring containing all the characters in the set.

For example, given the string "figehaeci" and the set of characters {a, e, i}, you should return "aeci".

If there is no substring containing all the characters in the set, return null.
"""

def is_sub_present(string, char_set):
    for element in char_set:
        if element in string:
            continue
        else:
            return(False)
    return(True)

def remove_from_front(string, char_set):
    if is_sub_present(string[1:], char_set):
        return remove_from_front(string[1:], char_set)
    else:
        return(string)

def remove_from_back(string, char_set):
    if is_sub_present(string[:len(string)-1], char_set):
        return remove_from_back(string[:len(string)-1], char_set)
    else:
        return(string)

def main():
    string, characters = raw_input("Enter string and substring?\n").split()
    char_set = set()
    for c in characters:
        char_set.add(c)

    if is_sub_present(string, char_set):
        string = remove_from_front(string, char_set)
        string = remove_from_back(string, char_set)
        print(string)
    else:
        print("null")

if __name__ == '__main__':
    main()