import sys
from collections import defaultdict

input = sys.stdin.readline

class Trie:
    def __init__(self):
        self.root = {}
        self.name = defaultdict(lambda: 1)

    def insert(self, S):
        current_node = self.root
        self.name[S] += 1
        for s in S:
            if s not in current_node:
                current_node[s] = {}
            current_node = current_node[s]
        current_node[-1] = True

    def search(self, S):
        current_node = self.root
        ret = []
        for s in S:
            ret.append(s)
            if s not in current_node:
                break
            current_node = current_node[s]
        nameCount = self.name[S]
        if len(S) == len(ret) and nameCount > 1:
            ret.append(str(nameCount))
        return "".join(ret)

trie = Trie()
for _ in range(int(input())):
    S = input().strip()
    print(trie.search(S))
    trie.insert(S)