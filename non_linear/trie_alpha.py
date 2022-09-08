from typing import List


class TrieNode:
    def __init__(self, data):
        self.data = data
        self.children = {}
        self.isEndOfWord = False  # True if node represents the end of a word


def output_children(parent_node: TrieNode, prefix_str: str = ""):
    all_children = [(parent_node, prefix_str)]
    output = []
    while all_children:
        parent, prefix_str = all_children.pop()
        if parent.isEndOfWord:
            output.append(f'{prefix_str}{parent.data}')
        if parent.children:
            for char, child in parent.children.items():
                all_children.append((child, f'{prefix_str}{parent.data}'))
    return output


class TrieClass:
    """
    Trie data structure class
    """
    def __init__(self):
        self.root = self.get_node()

    def get_node(self, data: str = '*') -> TrieNode:
        return TrieNode(data)  # returns new trie node (initialized to Nones)

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
                current.children[char] = self.get_node(char)
            current = current.children[char]
        current.isEndOfWord = True

    def does_word_exist(self, search_key: str) -> bool:
        current = self.root
        for char in search_key:
            if not current.children.get(char):
                return False
            current = current.children.get(char)
        return current.isEndOfWord

    def prefix_match(self, prefix_str: str) -> TrieNode:
        current = self.root
        output_node = None
        for char in prefix_str:
            if not current.children.get(char):
                return output_node
            current = current.children.get(char)
        return current


def main():
    # Input keys (use only 'a' through 'z' and lower case)
    keys = ["the", "a", "there", "anaswe", "any",
            "by", "their"]
    output = ["Not present in trie",
              "Present in trie"]

    # Trie object
    t = TrieClass()

    # Construct trie
    for key in keys:
        t.insert(key)

    # Search for different keys
    # print("{} ---- {}".format("the", output[t.does_word_exist("the")]))
    # print("{} ---- {}".format("these", output[t.does_word_exist("these")]))
    # print("{} ---- {}".format("their", output[t.does_word_exist("their")]))
    # print("{} ---- {}".format("thaw", output[t.does_word_exist("thaw")]))
    print(output_children(t.prefix_match('a')))


main()

