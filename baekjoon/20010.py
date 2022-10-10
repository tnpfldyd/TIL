from heapq import heappop, heappush
import sys
input = sys.stdin.readline
INF = sys.maxsize
N, M = map(int,input().split())
matrix = [[] for _ in range(N)]
matrix2 = [[] for _ in range(N)]
for _ in range(M):
    a, b, t = map(int, input().split())
    matrix[a].append((t, b))
    matrix[b].append((t, a))
visited = [False] * N
start = []
heappush(start, [0, 0, 0])
result, cnt = 0, 0
while start:
    x, node, last = heappop(start)
    if cnt == N:
        break
    if not visited[node]:
        visited[node] = True
        result += x
        cnt += 1
        if cnt != 1:
            matrix2[node].append((x, last))
            matrix2[last].append((x, node))
        for k, v in matrix[node]:
            heappush(start, [k, v, node])
answer = 0
for i in range(N):
    if len(matrix2[i]) == 1:
        start = []
        heappush(start, [0, i])
        visited = [INF] * N
        visited[i] = 0
        while start:
            x, node = heappop(start)
            if x > visited[node]:
                continue
            for k, v in matrix2[node]:
                nx = k + x
                if visited[v] > nx:
                    visited[v] = nx
                    heappush(start, [nx, v])
        if max(visited) > answer:
            answer = max(visited)
print(result)
print(answer)