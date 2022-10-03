from collections import deque
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
matrix = [list(input()) for _ in range(N)]
origin_key = {'a': '000001', 'b': '000010', 'c': '000100', 'd': '001000', 'e': '010000', 'f': '100000'}
buk = {'A': '000001', 'B': '000010', 'C': '000100', 'D': '001000', 'E': '010000', 'F': '100000'}
visited = [[[-1] * 64 for _ in range(M)] for _ in range(N)]
start = deque()
for i in range(N):
    for j in range(M):
        if matrix[i][j] == '0':
            start.append((i, j, '000000'))
            visited[i][j][0] = 0
dx, dy = [0,0,-1,1], [-1,1,0,0]
while start:
    x, y, key = start.popleft()
    if matrix[x][y] == '1':
        print(visited[x][y][int(key, 2)])
        break
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if matrix[nx][ny] in '0.1' and visited[nx][ny][int(key, 2)] == -1:
                visited[nx][ny][int(key, 2)] = visited[x][y][int(key, 2)] + 1
                start.append((nx, ny, key))
            elif matrix[nx][ny] in origin_key:
                new_key = ''
                temp = origin_key[matrix[nx][ny]]
                for j in range(6):
                    if key[j] == '1' or temp[j] == '1':
                        new_key += '1'
                    else:
                        new_key += '0'
                if visited[nx][ny][int(new_key, 2)] == -1:
                    visited[nx][ny][int(new_key, 2)] = visited[x][y][int(key, 2)] + 1
                    start.append((nx, ny, new_key))
            elif matrix[nx][ny] in buk:
                temp2 = buk[matrix[nx][ny]]
                for j in range(6):
                    if key[j] == '1' and temp2[j] == '1':
                        if visited[nx][ny][int(key, 2)] == -1:
                            visited[nx][ny][int(key, 2)] = visited[x][y][int(key, 2)] + 1
                            start.append((nx, ny, key))
                        break
else:
    print(-1)