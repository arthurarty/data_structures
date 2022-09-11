import math
import os
import random
import re
import sys

#
# Complete the 'contacts' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts 2D_STRING_ARRAY queries as parameter.
#
from collections import deque


class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEndOfWord = False
        self.counter = 0


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, input_str: str):
        current = self.root
        for char in input_str:
            index = ord(char) - ord('a')
            if not current.children[index]:
                current.children[index] = TrieNode()
            current.counter += 1
            current = current.children[index]
        current.isEndOfWord = True

    def prefix_match(self, input_str: str) -> int:
        current = self.root
        for char in input_str:
            index = ord(char) - ord('a')
            if current.children[index]:
                current = current.children[index]
            else:
                return 0
        return current.counter


def contacts(queries):
    trie_structure = Trie()
    result_list = []
    for query in queries:
        operation, value = query[0], query[1]
        if operation == 'add':
            trie_structure.add(value)
        elif operation == 'find':
            result_list.append(trie_structure.prefix_match(value))
    return result_list


if __name__ == '__main__':
    output = contacts([['add', 'hack'], ['add', 'hackerrank'], ['find', 'hac'], ['find', 'hak']])
    print(output)
    # queries_rows = int(input().strip())
    #
    # queries = []
    #
    # for _ in range(queries_rows):
    #     queries.append(input().rstrip().split())
    #
    # result = contacts(queries)
    # for res in result:
    #     print(res)
