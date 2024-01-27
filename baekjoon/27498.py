import sys
input = sys.stdin.readline

N, M = map(int, input().split())

edges = []
parent = [i for i in range(N + 1)]

result = 0

def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    x, y = find(a), find(b)
    if x > y:
        x, y = y, x
    parent[y] = x

for _ in range(M):
    a, b, c, d = map(int, input().split())
    if d:
        union(a, b)
        continue
    result += c
    edges.append((a, b, c))

edges.sort(key=lambda x : -x[2])

temp = 0
for i in range(len(edges)):
    s, e, cost = edges[i]
    if find(s) != find(e):
        union(s, e)
        temp += cost

print(result - temp)