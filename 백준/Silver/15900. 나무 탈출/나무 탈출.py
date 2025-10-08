import sys
sys.setrecursionlimit(600000)
input = sys.stdin.readline

N = int(input())
tree = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

answer = 0

def dfs(node, parent, depth):
    global answer
    
    for child in tree[node]:
        if child != parent:
            dfs(child, node, depth + 1)
    
    if len(tree[node]) == 1:
        answer += depth

dfs(1, 0, 0)
print("Yes" if answer % 2 == 1 else "No")