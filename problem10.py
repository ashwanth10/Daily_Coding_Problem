"""
Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, return all strings in the set that have s as a prefix.

For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].

Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.
"""

class TrieNode():
    def __init__(self):
        # Intialising one node for trie
        self.children = {}
        self.last = False


class Trie():
    def __init__(self):

        # Intialising the trie data structure
        self.root = TrieNode()
        self.word_list = []

    def formTrie(self, keys):
        """
        Forms a trie data structure with the given set of strings.
        :param keys:
        :return:
        """
        for key in keys:
            self.insert(key)

    def insert(self, key):
        """
        Inserts a key into Trie if it does not exist already.
        If the key is a prefix of the trie node, just mark it as leaf node.
        :param key:
        :return:
        """
        node = self.root
        for a in list(key):
            if not node.children.get(a):
                node.children[a] = TrieNode()
            node = node.children[a]
        node.last = True

    def suggestionsRec(self, node, word):
        if node.last:
            self.word_list.append(word)

        for a, n in node.children.items():
            self.suggestionsRec(n, word + a)

    def printAutoSuggestions(self, key):
        node = self.root
        not_found = False
        temp_word = ''

        for a in list(key):
            if not node.children.get(a):
                not_found = True
                break
            temp_word += a
            node = node.children[a]

        if not_found:
            return 0
        elif node.last and not node.children:
            return -1

        self.suggestionsRec(node, temp_word)
        for s in self.word_list:
            print(s)
        return 1


def main():
    set_of_strings = raw_input("enter strings?\n").split()
    query_string = raw_input("enter query string?\n")

    t = Trie()
    t.formTrie(set_of_strings)
    comp = t.printAutoSuggestions(query_string)

    if comp == 0:
        print("no strings found with this prefix")
    elif comp == -1:
        print("only key exists. no other string found.")

if __name__ == '__main__':
    main()