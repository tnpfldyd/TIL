import sys
input = sys.stdin.readline
N = int(input())
edges = []
parent = [i for i in range(N)]
N_list = [list(map(int, input().strip().split())) for _ in range(N)]
for i in range(N):
    for j in range(i+1, N):
        edges.append((N_list[i][j], i, j))

def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    if x < y:
        parent[y] = x
    else:
        parent[x] = y
edges.sort()
result = 0
for cost, a, b in edges:
    x, y = find(a), find(b)
    if x != y:
        union(x, y)
        result += cost
print(result)