import sys
input = sys.stdin.readline
INF = sys.maxsize

N, M = map(int, input().split())
edges = sorted([tuple(map(int, input().split())) for _ in range(M)], key=lambda x : x[2])
parents = [i for i in range(N + 1)]

def find(x):
    if x == parents[x]:
        return x
    parents[x] = find(parents[x])
    return parents[x]

def union(x, y):
    if x < y:
        x, y = y, x
    parents[x] = y

result = cnt = 0
    
for a, b, c in edges:
    x, y = find(a), find(b)
    if x != y:
        union(x, y)
        cnt += 1
        result = max(result, c)
    if cnt == N - 1:
        break
    
print(result)