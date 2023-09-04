import sys
input = sys.stdin.readline

class Node:
    def __init__(self):
        self.childNode = {}
    
    def push(self, x):
        node = self
        strings = x.split('\\')
        for string in strings:
            if string not in node.childNode:
                node.childNode[string] = Node()
            node = node.childNode[string]
    
    def printNodes(self, depth):
        node = self
        if node.childNode:
            keys = sorted(node.childNode.keys())
            for key in keys:
                print(" " * depth + key)
                node.childNode[key].printNodes(depth + 1)

N = int(input())
tree = Node()
for _ in range(N):
    line = input().strip()
    tree.push(line)

tree.printNodes(0)