from collections import deque
import sys
input = sys.stdin.readline
M, N, H = map(int, input().split())
matrix = [[list(map(int, input().rstrip().split())) for _ in range(N)] for _ in range(H)]
visited = [[[0] * M for _ in range(N)] for _ in range(H)]
start = deque()
for k in range(H):
    for i in range(N):
        for j in range(M):
            if matrix[k][i][j] == 1:
                start.append((k, i, j))
dx, dy, dz = [0,0,1,-1,0,0], [1,-1,0,0,0,0], [0,0,0,0,1,-1]
while start:
    z, y, x = start.popleft()
    for k in range(6):
        nx, ny, nz = x + dx[k], y + dy[k], z + dz[k]
        if 0 <= nx < M and 0 <= ny < N and 0 <= nz < H:
            if matrix[nz][ny][nx] == 0 and visited[nz][ny][nx] == 0:
                matrix[nz][ny][nx] = matrix[z][y][x] + 1
                visited[nz][ny][nx] = 1
                start.append((nz, ny, nx))
answer = True
result = 0
for i in range(H):
    for j in range(N):
        for k in range(M):
            if matrix[i][j][k] == 0:
                answer = False
            elif matrix[i][j][k] > result:
                result = matrix[i][j][k]
print(result-1 if answer else -1)