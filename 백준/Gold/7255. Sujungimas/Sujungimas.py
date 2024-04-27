import sys
input = sys.stdin.readline
INF = sys.maxsize

N, M = map(int, input().split())
pay = list(map(int, input().split()))
edges = []
for i in range(N - 1):
    for j in range(i + 1, N):
        cost = pay[i] * pay[j]
        edges.append((cost, i, j))

connections = [tuple(map(int, input().split())) for _ in range(M)]
for i, j in connections:
    edges.append((0, i - 1, j - 1))
    
edges.sort()
parents = [i for i in range(N)]
result = 0

def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])
    return parents[x]

def union(x, y):
    if x < y:
        x, y = y, x
    parents[x] = y

for c, a, b in edges:
    x, y = find(a), find(b)
    if x != y:
        union(x, y)
        result += c
        
print(result)        