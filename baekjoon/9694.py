from heapq import heappop, heappush
import sys
INF = sys.maxsize
input = sys.stdin.readline
T = int(input())
for i in range(1, T+1):
    M, N = map(int, input().split())
    matrix = [[] for _ in range(N)]
    for _ in range(M):
        a, b, t = map(int, input().split())
        matrix[a].append((t, b))
        matrix[b].append((t, a))
    visited = [INF] * N
    visited[0] = 0
    start = []
    temp = []
    heappush(start, [0, 0, [0]])
    while start:
        x, node, load = heappop(start)
        if x > visited[node]:
            continue
        for k, v in matrix[node]:
            nx = x + k
            if visited[v] > nx:
                visited[v] = nx
                heappush(start, [nx, v, load+[v]])
                if v == N-1:
                    temp = load+[v]
    print(f'Case #{i}:', end = ' ')
    if len(temp) != 0:
        print(*temp)
    else:
        print(-1)
