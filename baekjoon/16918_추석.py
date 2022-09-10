from collections import deque
import sys
input = sys.stdin.readline
N, M, end = map(int, input().split())
matrix = [list(input().rstrip()) for _ in range(N)]
cnt = 1
dx, dy = [0,0,1,-1], [1,-1,0,0]
for i in range(N):
    for j in range(M):
        if matrix[i][j] == 'O':
            matrix[i][j] = 1
while cnt < end:
    start = deque()
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == '.':
                matrix[i][j] = 0
            elif matrix[i][j] == 0 or matrix[i][j] == 1:
                matrix[i][j] += 1
            elif matrix[i][j] == 2:
                start.append((i, j))
                matrix[i][j] = '.'
    while start:
        x, y = start.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < N and 0 <= ny < M:
                matrix[nx][ny] = '.'
    cnt += 1
for i in range(N):
    for j in range(M):
        if matrix[i][j] != '.':
            matrix[i][j] = 'O'
for i in matrix:
    print(''.join(i))