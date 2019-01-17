"""
This problem was asked by Square.

Given a list of words, return the shortest unique prefix of each word. For example, given the list:
 dog, cat, apple, apricot, fish

Return the list:
 d, c, app, apr, f
"""

def prefix_exists(prefix, words):
    for w in words:
        if w.startswith(prefix):
            exists = True
            return exists
    return False

def main():
    words = raw_input("enter words?\n").split()
    unique_prefixs = []
    index = 1

    for i, word in enumerate(words):
        prefix = word[:index]
        while(True):
            if prefix_exists(prefix, words[:i] + words[i + 1:]):
                if index < len(word) - 1:
                    index += 1
                    prefix = word[:index]
                else:
                    index = 1
                    break
            else:
                unique_prefixs.append(prefix)
                break

    print(unique_prefixs)


if __name__ == '__main__':
    main()
