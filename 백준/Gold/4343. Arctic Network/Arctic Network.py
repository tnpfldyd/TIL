import sys
input = sys.stdin.readline

def find(x):
    if parents[x] == x:
        return x
    parents[x] = find(parents[x])
    return parents[x]

def union(a, b):
    if a < b:
        b, a = a, b
    parents[a] = b

N = int(input())

for _ in range(N):
    s, p = map(int, input().split())
    parents = [i for i in range(p + 1)]

    v = [list(map(int, input().split())) for _ in range(p)]

    edges = []
    for i in range(p):
        for j in range(i + 1, p):
            dist = ((v[i][0] - v[j][0]) ** 2 + (v[i][1] - v[j][1]) ** 2) ** 0.5
            edges.append((i, j, dist))

    edges.sort(key=lambda x: x[2])

    res = []
    for a, b, c in edges:
        a, b = find(a), find(b)
        if a != b:
            union(a, b)
            res.append(c)

    print(f'{res[-s]:.2f}')