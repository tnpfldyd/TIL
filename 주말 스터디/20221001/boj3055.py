from collections import deque
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
matrix = [list(input().rstrip()) for _ in range(N)]
start = deque()
Svisited = [[0] * M for _ in range(N)]
finish = []
for x in range(N):
    for y in range(M):
        if matrix[x][y] == 'S':
            start.append((x, y))
        elif matrix[x][y] == 'D':
            finish.append((x, y))
for x in range(N):
    for y in range(M):
        if matrix[x][y] == '*':
            start.append((x, y))
dx, dy = [0,0,1,-1],[1,-1,0,0]
while start:
    x, y = start.popleft()
    if matrix[finish[0][0]][finish[0][1]] == 'S':
        print(Svisited[finish[0][0]][finish[0][1]])
        break
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < N and 0 <= ny < M:
            if matrix[x][y] == 'S':
                if matrix[nx][ny] == '.' or matrix[nx][ny] == 'D':
                    Svisited[nx][ny] = Svisited[x][y] + 1
                    matrix[nx][ny] = 'S'
                    start.append((nx, ny))
            elif matrix[x][y] == '*':
                if matrix[nx][ny] == '.' or matrix[nx][ny] == 'S':
                    matrix[nx][ny] = '*'
                    start.append((nx, ny))
else:
    print('KAKTUS')