import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

def find(x):
    if parent[x] == -1:
        return x
    p = find(parent[x])
    dist[x] += dist[parent[x]]
    parent[x] = p
    return parent[x]

def union(x, y, z):
    root_x, root_y = find(x), find(y)
    if root_x == root_y:
        return
    dist[root_y] = dist[x] - dist[y] + z
    parent[root_y] = root_x
    
while True:
    N, M = map(int, input().split())
    if not N and not M:
        break
    parent = [-1] * (N + 1)
    dist = [0] * (N + 1)
    for _ in range(M):
        order, *num = list(input().strip().split())
        if order == '!':
            a, b, c = map(int, num)
            union(a, b, c)
        else:
            a, b = map(int, num)
            if find(a) != find(b):
                print("UNKNOWN")
            else:
                print(dist[b] - dist[a])