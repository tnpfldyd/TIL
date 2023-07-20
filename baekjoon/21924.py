from heapq import heappop, heappush
import sys
input = sys.stdin.readline

def find(x):
    if x == parent[x]:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    if x < y:
        x, y = y, x
    parent[x] = y

N, M = map(int, input().split())
edges = []
total = 0
parent = [i for i in range(N + 1)]
for _ in range(M):
    a, b, t = map(int, input().split())
    total += t
    heappush(edges, (t, a, b))

cnt = 0
result = 0
while edges:
    t, a, b = heappop(edges)
    if cnt == N - 1:
        print(total - result)
        break
    a, b = find(a), find(b)
    if a != b:
        union(a, b)
        cnt += 1
        result += t
else:
    print(-1)