from heapq import heappop, heappush
from collections import deque
import sys
input = sys.stdin.readline
INF = sys.maxsize

N, M = map(int, input().split())
matrix = [list(input().strip()) for _ in range(N)]
cnt = 0
for i in range(N):
    for j in range(N):
        if matrix[i][j] == 'S':
            matrix[i][j] = cnt
            S = cnt
            cnt += 1
        elif matrix[i][j] == 'K':
            matrix[i][j] = cnt
            cnt += 1
edges = []
answer = False
dx, dy = [0,0,-1,1],[1,-1,0,0]
for i in range(N):
    for j in range(N):
        if isinstance(matrix[i][j], int):
            visited = [[False] * N for _ in range(N)]
            visited[i][j] = True
            start = deque()
            start.append((i, j))
            temp = matrix[i][j]
            node_cnt, distance = 0, 1
            while start:
                for _ in range(len(start)):
                    x, y = start.popleft()
                    for k in range(4):
                        nx, ny = x + dx[k], y + dy[k]
                        if 0 <= nx < N and 0 <= ny < N and matrix[nx][ny] != '1' and not visited[nx][ny]:
                            visited[nx][ny] = True
                            if isinstance(matrix[nx][ny], int):
                                node_cnt += 1
                                start.append((nx, ny))
                                edges.append((temp, matrix[nx][ny], distance))
                            else:
                                start.append((nx, ny))
                distance += 1
            if node_cnt != M:
                answer = True
if answer:
    print(-1)
else:
    matrix = [[] for _ in range(M+1)]
    for a, b, t in edges:
        matrix[a].append((t, b))
    visited = [False] * (M+1)
    start = []
    heappush(start, [0, S])
    result, cnt = 0, 0
    while start:
        x, node = heappop(start)
        if cnt == M+1:
            break
        if not visited[node]:
            visited[node] = True
            cnt += 1
            result += x
            for k, v in matrix[node]:
                heappush(start, [k, v])
    print(result)