from collections import deque
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
matrix = [list(input().strip()) for _ in range(N)]
sx, sy = 0, 0
cnt = 1
for i in range(N):
    for j in range(M):
        if matrix[i][j] == 'S':
            sx, sy = i, j
            matrix[i][j] = '.'
        elif matrix[i][j] == 'C':
            matrix[i][j] = bin(cnt)[2:]
            if len(matrix[i][j]) < 2:
                matrix[i][j] = '0' + matrix[i][j]
            cnt *= 2
visited = [[[[-1] * 4 for _ in range(M)] for _ in range(N)] for _ in range(4)]
start = deque()
dx, dy = [0,0,1,-1], [1,-1,0,0]
for i in range(4):
    start.append((sx, sy, '00', i))
    visited[i][sx][sy][0] = 0
while start:
    x, y, key, dir = start.popleft()
    if key == '11':
        print(visited[dir][x][y][int(key, 2)])
        break
    for i in range(4):
        if i == dir:
            continue
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if matrix[nx][ny] != '#':
                if matrix[nx][ny] == '.' and visited[i][nx][ny][int(key, 2)] == -1:
                    visited[i][nx][ny][int(key, 2)] = visited[dir][x][y][int(key, 2)] + 1
                    start.append((nx, ny, key, i))
                elif matrix[nx][ny] == '01' or matrix[nx][ny] == '10':
                    new_key = ''
                    for k in range(2):
                        if key[k] == '1' or matrix[nx][ny][k] == '1':
                            new_key += '1'
                        else:
                            new_key += '0'
                    if visited[i][nx][ny][int(new_key, 2)] == -1:
                        visited[i][nx][ny][int(new_key, 2)] = visited[dir][x][y][int(key, 2)] + 1
                        start.append((nx, ny, new_key, i))
else:
    print(-1)