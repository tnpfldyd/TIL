from heapq import heappop, heappush
import sys
input = sys.stdin.readline
INF = sys.maxsize
while True:
    N, M, S, C = map(int, input().split())
    if not N and not M and not S and not C:
        break
    matrix = [[] for _ in range(N + 1)]
    for _ in range(M):
        a, b, c = map(int, input().split())
        matrix[a].append((c, b))
        
    pq = [(0, S)]
    visited = [INF] * (N + 1)
    visited[S] = 0
    while pq:
        c, x = heappop(pq)
        if visited[x] < c:
            continue
        for nc, nx in matrix[x]:
            a = nc + c
            if visited[nx] > a:
                visited[nx] = a
                heappush(pq, (a, nx))
    print(visited[C])