import sys
input = sys.stdin.readline

N, M = map(int, input().split())
parent = [i for i in range(N + 1)]

def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    if x > y:
        x, y = y, x
    parent[x] = y

for _ in range(M):
    a, b = map(int, input().split())
    x, y = find(a), find(b)
    if x != y: 
        union(x, y)

edges = []

for i in range(N):
    arr = list(map(int, input().split()))
    for j in range(N):
        if i and j and i != j:
            edges.append((arr[j], i + 1, j + 1))

edges.sort()
result = []
answer = 0

for edge in edges:
    cost, a, b = edge
    x, y = find(a), find(b)
    if x != y:
        union(x, y)
        result.append((a, b))
        answer += cost
print(answer, len(result))
for nodes in result:
    print(*nodes)