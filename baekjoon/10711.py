from collections import deque
import sys

input = sys.stdin.readline
N, M = map(int, input().split())
matrix = [list(input().rstrip()) for _ in range(N)]
start = deque()
for i in range(N):
    for j in range(M):
        if matrix[i][j] == ".":
            start.append((i, j))
dx, dy = [0, 0, 1, -1, -1, 1, -1, 1], [1, -1, 0, 0, 1, 1, -1, -1]
visited = [[0] * M for _ in range(N)]
while start:
    x, y = start.popleft()
    for i in range(8):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if matrix[nx][ny] != "." and matrix[nx][ny] != 0:
                matrix[nx][ny] = int(matrix[nx][ny]) - 1
                if not matrix[nx][ny]:
                    visited[nx][ny] = visited[x][y] + 1
                    start.append((nx, ny))
print(max(map(max, visited)))
