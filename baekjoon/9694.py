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
    heappush(start, (0, 0, [0]))
    print(f'Case #{i}:', end = ' ')
    while start:
        x, node, load = heappop(start)
        if x > visited[node]:
            continue
        if node == N - 1:
            print(*load)
            break
        for k, v in matrix[node]:
            nx = x + k
            nload = load + [v]
            if visited[v] > nx:
                visited[v] = nx
                heappush(start, (nx, v, nload))
    else:
        print(-1)
