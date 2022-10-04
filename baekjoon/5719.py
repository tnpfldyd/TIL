from heapq import heappop, heappush
import sys
input = sys.stdin.readline
INF = sys.maxsize
while True:
    N, M = map(int, input().split())
    if N == 0 and M == 0:
        break
    s, e = map(int, input().split())
    matrix = [[] for _ in range(N)]
    rev_matrix = [[] for _ in range(N)]
    temp = set()
    for i in range(M):
        a, b, t = map(int, input().split())
        matrix[a].append((t, b, i))
        rev_matrix[b].append((t, a, i))
    visited = [INF] * N
    visited[s] = 0
    start = []
    heappush(start, [0, s])
    while start:
        x, node = heappop(start)
        if x > visited[node]:
            continue
        for k, v, l in matrix[node]:
            nx = x + k
            if visited[v] > nx:
                visited[v] = nx
                heappush(start, [nx, v])
    heappush(start, [0, e])
    while start:
        x, node = heappop(start)
        if node == s:
            continue
        for k, v, l in rev_matrix[node]:
            if l in temp:
                continue
            if visited[v] == visited[node] - k:
                temp.add(l)
                heappush(start, [visited[v], v])
    heappush(start, [0, s])
    visited2 = [INF] * N
    visited2[s] = 0
    while start:
        x, node = heappop(start)
        if x > visited2[node]:
            continue
        for k, v, l in matrix[node]:
            nx = x + k
            if visited2[v] > nx and l not in temp:
                visited2[v] = nx
                heappush(start, [nx, v])
    print(visited2[e] if visited2[e] != INF else -1)