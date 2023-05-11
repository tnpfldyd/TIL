from heapq import heappop, heappush
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
parent = [i for i in range(N + 1)]
god = [tuple(map(int, input().split())) for _ in range(N)]
connect = [tuple(map(int, input().split())) for _ in range(M)]

def find(x):
    if x == parent[x]:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a, b = find(a), find(b)
    parent[b] = a

def get_dist(x1, y1, x2, y2):
    return (abs(x1 - x2) ** 2 + abs(y1 - y2) ** 2) ** 0.5

for i in range(M):
    x, y = connect[i]
    x -= 1; y -= 1
    a, b = find(x), find(y)
    if a != b:
        union(x, y)

edges = []

for i in range(N - 1):
    x1, y1 = god[i]
    for j in range(i + 1, N):
        x2, y2 = god[j]
        dist = get_dist(x1, y1, x2, y2)
        heappush(edges, (dist, i, j))

result = 0

while edges:
    cost, a, b = heappop(edges)
    x, y = find(a), find(b)
    if x != y:
        union(a, b)
        result += cost
print(f'{result:.2f}')