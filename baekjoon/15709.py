from heapq import heappop, heappush
import sys
input = sys.stdin.readline
INF = sys.maxsize
N, M, B, K, Q = map(int, input().split())
matrix = [[] for _ in range(N+M+B)]
for _ in range(K):
    a, b, t = map(int, input().split())
    a -= 1; b -= 1
    matrix[a].append((t, b))
    matrix[b].append((t, a))


def dijkstra(s):
    start = []
    heappush(start, (0, s+N+M))
    visited = [INF] * (N+M+B)
    visited[s+N+M] = 0
    while start:
        cost, node = heappop(start)
        if cost > visited[node]:
            continue
        for k, v in matrix[node]:
            nx = cost + k
            if visited[v] > nx:
                visited[v] = nx
                heappush(start, (nx, v))
    return visited
visited = []
for i in range(B):
    visited.append(dijkstra(i))
for _ in range(Q):
    a, b = map(int, input().split())
    a -= 1; b -= 1
    answer = INF
    for i in range(B):
        answer = min(answer, visited[i][a] + visited[i][b])
    print(answer if answer != INF else -1)