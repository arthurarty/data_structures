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
    def __init__(self, data=None):
        self.data = data
        self.children = {}
        self.isEndOfWord = False
        self.counter = 0


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, input_str: str):
        current = self.root
        for char in input_str:
            if current.children.get(char) is None:
                current.children[char] = TrieNode(char)
            current.counter += 1
            current = current.children.get(char)
        current.isEndOfWord = True

    def prefix_match(self, input_str: str) -> int:
        current = self.root
        count = 0
        for char in input_str:
            if char in current.children.keys():
                current = current.children.get(char)
            else:
                return 0
        if current.isEndOfWord:
            count += 1
        return current.counter + count


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
    output = contacts([
        ['add', 's'],
        ['add', 'ss'],
        ['add', 'sss'],
        ['add', 'ssss'],
        ['add', 'sssss'],
        ['find', 's'],
        ['find', 'ss'],
        ['find', 'sss'],
        ['find', 'ssss'],
        ['find', 'sssss'],
        ['find', 'ssssss']
    ])
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
