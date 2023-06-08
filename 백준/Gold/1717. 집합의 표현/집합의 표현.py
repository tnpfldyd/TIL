import sys
input = sys.stdin.readline
N, M = map(int, input().split())

parent = [i for i in range(N + 1)]

def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a, b = find(a), find(b)
    if a > b:
        parent[b] = a
    else:
        parent[a] = b
for _ in range(M):
    o, a, b = map(int, input().split())
    if not o:
        union(a, b)
    else:
        print("NO" if find(a) != find(b) else "YES")