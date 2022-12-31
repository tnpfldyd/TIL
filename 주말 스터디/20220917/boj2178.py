N, M = map(int, input().split())
matrix = [list(map(int, input())) for _ in range(N)]
result = [[0]*M for _ in range(N)]
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
start = [(N-1, M-1)]
result[N-1][M-1] = 1

while start:
    x, y = start.pop(0)
    if x == 0 and y == 0:
        print(result[x][y])
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if result[nx][ny] == 0 and matrix[nx][ny] == 1:
                result[nx][ny] = result[x][y] + 1
                start.append((nx, ny))