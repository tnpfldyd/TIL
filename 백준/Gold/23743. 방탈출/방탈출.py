import sys
input = sys.stdin.readline
N, M = map(int, input().split())
parent = [i for i in range(N+1)]
edges = []
for _ in range(M):
    a, b, t = map(int, input().split())
    edges.append((t, a, b))
cost_list = [0] + list(map(int, input().strip().split()))
for i in range(1, N+1):
    edges.append((cost_list[i], 0, i))
edges.sort()
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

result = 0

for edge in edges:
    cost, x, y = edge
    x = find(x); y = find(y)
    if x != y:
        union(x, y)
        result += cost
print(result)