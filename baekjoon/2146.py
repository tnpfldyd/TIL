from collections import deque
import sys
input = sys.stdin.readline
N = int(input())
matrix = [list(map(int, input().rstrip().split())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]
twostart = []
cnt = 1
dx, dy = [0,0,-1,1],[1,-1,0,0]
for i in range(N):
    for j in range(N):
        if matrix[i][j] == 1 and not visited[i][j]:
            start = deque()
            start.append((i, j))
            matrix[i][j] = cnt
            visited[i][j] = True
            while start:
                x, y = start.popleft()
                cnt0 = 0
                for k in range(4):
                    nx, ny = x + dx[k], y + dy[k]
                    if 0 <= nx < N and 0 <= ny < N and matrix[nx][ny] == 1 and not visited[nx][ny]:
                        matrix[nx][ny] = cnt
                        visited[nx][ny] = True
                        start.append((nx, ny))
                    if 0 <= nx < N and 0 <= ny < N and matrix[nx][ny] == 0:
                        cnt0 += 1
                if cnt0 > 0:
                    twostart.append((x, y))
            cnt += 1
reture = []
def bfs(i):
    twst = deque()
    twst.append(i)
    q, w = i
    visited2 = [[0] * N for _ in range(N)]
    while twst:
        x, y = twst.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < N and 0 <= ny < N and visited2[nx][ny] == 0 and matrix[nx][ny] == 0:
                visited2[nx][ny] = visited2[x][y] + 1
                twst.append((nx, ny))
            elif 0 <= nx < N and 0 <= ny < N and visited2[nx][ny] == 0 and matrix[nx][ny] != matrix[q][w] and matrix[nx][ny] != 0:
                return visited2[x][y]
for i in twostart:
    reture.append(bfs(i))
qwqw = 10000
for i in reture:
    if i != None and qwqw > i:
        qwqw = i
print(qwqw)
