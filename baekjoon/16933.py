from collections import deque
import sys
input = sys.stdin.readline
N, M, K = map(int, input().split())
matrix = [list(map(int, input().rstrip())) for _ in range(N)]
visited = [[[-1] * (K+1) for _ in range(M)] for _ in range(N)]
start = deque()
start.append((0, 0, 0, 0))
visited[0][0][0] = 1
dx, dy = [0,0,-1,1], [1,-1,0,0]
while start:
    x, y, k, day = start.popleft()
    if x == N-1 and y == M-1:
        print(visited[x][y][k])
        break
    if day == 1:
        visited[x][y][k] += 1
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if visited[nx][ny][k] == -1:
                if matrix[nx][ny] == 0:
                    visited[nx][ny][k] = visited[x][y][k] + 1
                    start.append((nx, ny, k, 0))
                elif k < K and visited[nx][ny][k+1] == -1:
                    if visited[x][y][k] % 2 == 0:
                        start.append((x, y, k, 1))
                    else:
                        visited[nx][ny][k+1] = visited[x][y][k] + 1
                        start.append((nx, ny, k + 1, 0))
else:
    print(-1)