"""
Trie data structure is a type of tree where each node is a character.
Trie is good for problems involving finding substrings and string validation.
Good for making contact list applications.
Good for auto complete.
"""
from typing import List


class TrieNode:
    def __init__(self):
        self.children = [None] * 26  # 26 letters of the alphabet
        self.isEndOfWord = False  # True if node represents the end of a word


class Trie:
    """
    Trie data structure class
    """
    def __init__(self):
        self.root = self.get_node()

    def get_node(self) -> TrieNode():
        return TrieNode()  # returns new trie node (initialized to Nones)

    def _char_to_index(self, ch: str) -> int:
        """
        Covert a character/key to int representation.
        Understand the ord function used - https://www.w3schools.com/python/ref_func_ord.asp
        However we also want to know how far it is from the start. i.e distance from Letter `a`
        :param ch:
        :return:
        """
        ch = ch.lower()
        return ord(ch) - ord('a')

    def insert(self, input_str: str):
        """
        If not present, inserts input_str into trie
        If the key is prefix of trie node, makes leave node.
        :param input_str:
        :return:
        """
        current = self.root
        for ii in range(len(input_str)):
            index = self._char_to_index(input_str[ii])
            # if current character is not present in current node's children
            if not current.children[index]:
                current.children[index] = self.get_node()
            current = current.children[index]
        current.isEndOfWord = True

    def does_word_exist(self, search_key: str) -> bool:
        current = self.root
        for ii in range(len(search_key)):
            index = self._char_to_index(search_key[ii])
            if not current.children[index]:
                return False
            current = current.children[index]
        return current.isEndOfWord


def main():
    # Input keys (use only 'a' through 'z' and lower case)
    keys = ["the", "a", "there", "anaswe", "any",
            "by", "their"]
    output = ["Not present in trie",
              "Present in trie"]

    # Trie object
    t = Trie()

    # Construct trie
    for key in keys:
        t.insert(key)

    # Search for different keys
    print("{} ---- {}".format("the", output[t.does_word_exist("the")]))
    print("{} ---- {}".format("these", output[t.does_word_exist("these")]))
    print("{} ---- {}".format("their", output[t.does_word_exist("their")]))
    print("{} ---- {}".format("thaw", output[t.does_word_exist("thaw")]))


if __name__ == '__main__':
    main()
