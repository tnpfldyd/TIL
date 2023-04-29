import sys
input = sys.stdin.readline
T = int(input())

def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)
    if x != y:
        if size[x] < size[y]:
            x, y = y, x
        size[x] += size[y]
        parent[y] = x

for _ in range(T):
    M = int(input())
    name = {}
    size = [1] * ((M * 2) + 1)
    parent = [i for i in range((M * 2) + 1)]
    cnt = 1
    for _ in range(M):
        a, b = input().split()
        if a not in name:
            name[a] = cnt
            cnt += 1
        if b not in name:
            name[b] = cnt
            cnt += 1
        union(name[a], name[b])
        x, y = find(name[a]), find(name[b])
        print(max(size[x], size[y]))
    