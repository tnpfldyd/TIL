import sys
input = sys.stdin.readline
N = int(input())
edges = []
parents = [*range(N)]

def find(x):
    if parents[x] == x:
        return x
    parents[x] = find(parents[x])
    return parents[x]

def union(x, y):
    x, y = find(x), find(y)
    if x > y:
        x, y = y, x
    parents[x] = y
cnt = 0
result = 0
for i in range(N):
    row = list(map(int, input().split()))
    for j in range(i + 1, N):
        if not row[j]:
            continue
        if row[j] < 0:
            union(i, j)
            result += -row[j]
        else:
            edges.append((row[j], i, j))
            
edges.sort()
points = []
for c, a, b in edges:
    if find(a) != find(b):
        result += c
        points.append((a, b))
        union(a, b)
        cnt += 1

print(result, len(points))
for x, y in points:
    print(x + 1, y + 1)