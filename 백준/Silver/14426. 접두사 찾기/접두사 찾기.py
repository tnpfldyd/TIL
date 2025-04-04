class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]

    def starts_with_prefix(self, word):
        node = self.root
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                return False
        return True

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

trie = Trie()

for _ in range(n):
    s = input().strip()
    trie.insert(s)

count = 0
for _ in range(m):
    query = input().strip()
    if trie.starts_with_prefix(query):
        count += 1

print(count)