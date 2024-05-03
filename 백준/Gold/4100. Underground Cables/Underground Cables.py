import sys
input = sys.stdin.readline

while True:
    M = int(input())
    if not M:
        break
    parents = [i for i in range(M)]

    def find(x):
        if x == parents[x]:
            return x
        parents[x] = find(parents[x])
        return parents[x]

    def union(x, y):
        if x < y:
            x, y = y, x
        parents[x] = y
        
    points = [tuple(map(int, input().split())) for _ in range(M)]
    edges = []
    for i in range(M - 1):
        x1, y1 = points[i]
        for j in range(i + 1, M):
            x2, y2 = points[j]
            cost = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
            edges.append((cost, i, j))
            
    edges.sort()
    result = cnt = 0
    for c, a, b in edges:
        x, y = find(a), find(b)
        if x != y:
            union(x, y)
            result += c
            cnt += 1
        if cnt == M - 1:
            break
    print(f'{result:.2f}')