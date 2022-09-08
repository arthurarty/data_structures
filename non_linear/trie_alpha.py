from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False  # True if node represents the end of a word


class Trie:
    """
    Trie data structure class
    """
    def __init__(self):
        self.root = self.get_node()

    def get_node(self) -> TrieNode():
        return TrieNode()  # returns new trie node (initialized to Nones)

    def insert(self, input_str: str):
        """
        If not present, inserts input_str into trie
        If the key is prefix of trie node, makes leave node.
        :param input_str:
        :return:
        """
        current = self.root
        for char in input_str:
            # if current character is not present in current node's children
            if not current.children.get(char):
                current.children[char] = self.get_node()
            current = current.children[char]
        current.isEndOfWord = True

    def does_word_exist(self, search_key: str) -> bool:
        current = self.root
        for char in search_key:
            if not current.children.get(char):
                return False
            current = current.children.get(char)
        return current.isEndOfWord

    # def prefix_match(self, prefix_str: str) -> List[str]:
    #     current = self.root
    #     output_list = []
    #     for ii in range(len(prefix_str)):
    #         index = self._char_to_index(prefix_str[ii])
    #         if not current.children[index]:
    #             return output_list
    #         if current.isEndOfWord and ii == 0:
    #             output_list.append()
    #     return []


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
