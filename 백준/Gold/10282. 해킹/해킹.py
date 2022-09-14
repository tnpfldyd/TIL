from heapq import heappop, heappush
import sys
INF = sys.maxsize
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N, M, s = map(int, input().split())
    visited = [INF] * N
    matrix = [[] for _ in range(N)]
    for _ in range(M):
        a, b, t = map(int, input().split())
        matrix[b-1].append((t, a-1))
    start = []
    heappush(start, [0, s-1])
    visited[s-1] = 0
    while start:
        x, node = heappop(start)
        if x > visited[node]:
            continue
        for k, v in matrix[node]:
            nx = x + k
            if visited[v] > nx:
                visited[v] = nx
                heappush(start, [nx, v])
    max_cnt = 0
    cnt = 0
    for i in visited:
        if i != INF:
            cnt += 1
            if max_cnt < i:
                max_cnt = i
    print(cnt, max_cnt)