import sys
input = sys.stdin.readline
N, M = map(int, input().split())
country_cost = [0] * (N + 1)
result = sys.maxsize
for i in range(1, N + 1):
    country_cost[i] = int(input())
    result = min(result, country_cost[i])
edges = []
for i in range(M):
    a, b, pay = map(int, input().split())
    cost = country_cost[a] + country_cost[b] + pay * 2
    edges.append((cost, a, b))
edges.sort()
parent = [i for i in range(N + 1)]
cnt = 0

def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x, y = find(x), find(y)
    if x < y:
        parent[y] = x
    else:
        parent[y] = x

for edge in edges:
    cost, a, b = edge
    if find(a) != find(b):
        union(a, b)
        cnt += 1
        result += cost
    if cnt == N - 1:
        break
print(result)