import sys
input = sys.stdin.readline
N, K = map(int, input().split())

names = [input().strip() for _ in range(N)]
edges = []
for i in range(N - 1):
    a = names[i]
    for j in range(i + 1, N):
        b = names[j]
        c = 0
        for k in range(K):
            c += abs(ord(a[k]) - ord(b[k]))
        edges.append((c, i, j))
        
edges.sort()
parents = [*range(N)]

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
for c, a, b in edges:
    x, y = find(a), find(b)
    if x != y:
        union(x, y)
        cnt += 1
        result = max(result, c)
    if cnt == N - 1:
        break

print(result)