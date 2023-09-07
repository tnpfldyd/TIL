from heapq import heappush, heappop
import sys
input = sys.stdin.readline

N, C = map(int, input().split())

nodes = [tuple(map(int, input().split())) for _ in range(N)]

edges = []

for i in range(N - 1):
    for j in range(i + 1, N):
        x1, y1 = nodes[i]
        x2, y2 = nodes[j]
        cost = (x1 - x2) ** 2 + (y1 - y2) ** 2
        if cost >= C:
            heappush(edges, (cost, i, j))

def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    if x > y:
        x, y = y, x
    parent[x] = y

result = 0
cnt = 0
parent = [i for i in range(N)]
while edges:
    cost, a, b = heappop(edges)
    x, y = find(a), find(b)
    if x != y:
        union(x, y)
        result += cost
        cnt += 1
        if cnt + 1 == N:
            print(result)
            break
else:
    print(-1)