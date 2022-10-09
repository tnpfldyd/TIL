from heapq import heappop, heappush
from collections import deque
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
matrix = [list(map(int, input().rstrip().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
p = 0
dx, dy = [0,0,1,-1], [1,-1,0,0]
one = deque()
edges = []
for i in range(N):
    for j in range(M):
        if matrix[i][j] == 1 and not visited[i][j]:
            p += 1
            visited[i][j] = True
            start = deque()
            start.append((i, j))
            one.append((i, j, p))
            matrix[i][j] = p
            while start:
                x, y = start.popleft()
                for k in range(4):
                    nx, ny = x + dx[k], y + dy[k]
                    if 0 <= nx < N and 0 <= ny < M:
                        if not visited[nx][ny] and matrix[nx][ny] == 1:
                            matrix[nx][ny] = p
                            one.append((nx, ny, p))
                            start.append((nx, ny))
                            visited[nx][ny] = True
while one:
    x, y, e = one.popleft()
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < N and 0 <= ny < M:
            if matrix[nx][ny] == 0:
                cnt = 1
                while 0 <= nx + dx[k] < N and 0 <= ny + dy[k] < M:
                    nx, ny = nx + dx[k], ny + dy[k]
                    if matrix[nx][ny] == 0:
                        cnt += 1
                    else:
                        if cnt >= 2 and matrix[nx][ny] != e:
                            edges.append((e, matrix[nx][ny], cnt))
                        break
temp = [[] for _ in range(p)]
for a, b, t in edges:
    a -= 1; b -= 1
    temp[a].append((t, b))
    temp[b].append((t, a))
visit = [False] * p
start = []
heappush(start, [0, 0])
cnt = 0; stat = 0
while start:
    x, node = heappop(start)
    if stat == p:
        break
    if not visit[node]:
        visit[node] = True
        stat += 1
        cnt += x
        for k, v in temp[node]:
            heappush(start, [k, v])
if stat == p:
    print(cnt)
else:
    print(-1)