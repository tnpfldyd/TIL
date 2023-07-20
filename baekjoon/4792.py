import sys
input = sys.stdin.readline

def kruskal(edges):
    
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
            parent[x] = y

    parent = [i for i in range(N + 1)]
    val = 0
    for cost, a, b in edges:
        if find(a) != find(b):
            union(a, b)
            val += cost
    return val

while True:
    N, M, K = map(int, input().split())

    if not N and not M and not K:
        break

    min_max_edges = [[], []]

    for i in range(M):
        color, u, v = input().split()
        u, v = int(u), int(v)
        c = 1 if color == 'B' else 0
        min_max_edges[0].append((c, u, v))
        min_max_edges[1].append((c, u, v))
    min_max_edges[0].sort()
    min_max_edges[1].sort(key=lambda x : -x[0])
    min_blue, max_blue = kruskal(min_max_edges[0]), kruskal(min_max_edges[1])
    if min_blue <= K <= max_blue:
        print(1)
    else:
        print(0)
