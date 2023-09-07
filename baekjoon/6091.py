from heapq import heappush, heappop
import sys
input = sys.stdin.readline

def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x, y = find(x), find(y)
    if x == y:
        return False
    parent[x] = y
    return True


N = int(input())
parent = [i for i in range(N + 1)]

pq = []
for i in range(1, N):
    arr = list(map(int, input().strip().split()))
    for j, cost in zip(range(i + 1, N + 1), arr):
        heappush(pq, (cost, i, j))

matrix = [[] for _ in range(N + 1)]

while pq:
    cost, a, b = heappop(pq)
    if union(a, b):
        matrix[a].append(b)
        matrix[b].append(a)

for arr in matrix[1:]:
    print(len(arr), *sorted(arr))