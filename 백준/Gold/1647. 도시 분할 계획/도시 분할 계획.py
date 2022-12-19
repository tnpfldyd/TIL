from heapq import heappop, heappush
import sys
input = sys.stdin.readline

def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y
N, M = map(int, input().split())
parent = [i for i in range(N+1)]
edges = []
for _ in range(M):
    a, b, t = map(int, input().split())
    heappush(edges, (t, a, b))
result = 0
max_num = 0
for _ in range(M):
    cost, a, b = heappop(edges)
    if find(a) != find(b):
        union(a, b)
        result += cost
        if max_num < cost:
            max_num = cost
print(result - max_num)