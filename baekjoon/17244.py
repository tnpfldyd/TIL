from collections import deque
import sys

input = sys.stdin.readline
M, N = map(int, input().split())
matrix = [list(input().rstrip()) for _ in range(N)]
cnt = 1
sx, sy, ex, ey = 0, 0, 0, 0
keyset = set()
for i in range(N):
    for j in range(M):
        if matrix[i][j] == "S":
            sx, sy = i, j
            matrix[i][j] = "."
        elif matrix[i][j] == "X":
            matrix[i][j] = cnt
            cnt *= 2
        elif matrix[i][j] == "E":
            ex, ey = i, j
            matrix[i][j] = "."
dx, dy = [0, 0, -1, 1], [1, -1, 0, 0]
if cnt == 1:
    start = deque()
    start.append((sx, sy))
    visited = [[-1] * M for _ in range(N)]
    visited[sx][sy] = 0
    while start:
        x, y = start.popleft()
        if x == ex and y == ey:
            print(visited[x][y])
            break
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if matrix[nx][ny] == "." and visited[nx][ny] == -1:
                    visited[nx][ny] = visited[x][y] + 1
                    start.append((nx, ny))
else:
    temp = bin(cnt)[3:]
    for i in range(N):
        for j in range(M):
            if isinstance(matrix[i][j], int):
                matrix[i][j] = bin(matrix[i][j])[2:]
                while len(matrix[i][j]) < len(temp):
                    matrix[i][j] = "0" + matrix[i][j]
                keyset.add(matrix[i][j])
    visited = [[[-1] * cnt for _ in range(M)] for _ in range(N)]
    visited[sx][sy][0] = 0
    start = deque()
    start.append((sx, sy, temp))
    while start:
        x, y, key = start.popleft()
        if "0" not in key and x == ex and y == ey:
            print(visited[x][y][int(key, 2)])
            break
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if matrix[nx][ny] == "." and visited[nx][ny][int(key, 2)] == -1:
                    visited[nx][ny][int(key, 2)] = visited[x][y][int(key, 2)] + 1
                    start.append((nx, ny, key))
                elif matrix[nx][ny] in keyset:
                    new_key = ""
                    for j in range(len(key)):
                        if key[j] == "1" or matrix[nx][ny][j] == "1":
                            new_key += "1"
                        else:
                            new_key += "0"
                    if visited[nx][ny][int(new_key, 2)] == -1:
                        visited[nx][ny][int(new_key, 2)] = visited[x][y][int(key, 2)] + 1
                        start.append((nx, ny, new_key))
