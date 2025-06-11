import sys
input = sys.stdin.readline

N = int(input())
tree = {}

for _ in range(N):
    root, left, right = input().split()
    tree[root] = [left, right]

def preorder(node):
    if node == '.':
        return ''
    return node + preorder(tree[node][0]) + preorder(tree[node][1])

def inorder(node):
    if node == '.':
        return ''
    return inorder(tree[node][0]) + node + inorder(tree[node][1])

def postorder(node):
    if node == '.':
        return ''
    return postorder(tree[node][0]) + postorder(tree[node][1]) + node

print(preorder('A'))
print(inorder('A'))
print(postorder('A'))