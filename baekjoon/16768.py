from collections import deque
import sys
input = sys.stdin.readline
N, K = map(int, input().split())
matrix = [list(input().rstrip()) for _ in range(N)]
dx, dy = [0,0,1,-1], [1,-1,0,0]
while True:
    visited = [[False] * 10 for _ in range(N)]
    zero = set()
    for i in range(N):
        for j in range(10):
            if not visited[i][j] and matrix[i][j] != '0':
                start = deque()
                temp = []
                visited[i][j] = True
                start.append((i, j))
                temp.append((i, j))
                while start:
                    x, y = start.popleft()
                    for k in range(4):
                        nx, ny = x + dx[k], y + dy[k]
                        if 0 <= nx < N and 0 <= ny < 10:
                            if matrix[nx][ny] == matrix[i][j] and not visited[nx][ny]:
                                visited[nx][ny] = True
                                start.append((nx, ny))
                                temp.append((nx, ny))
                if len(temp) >= K:
                    for k, v in temp:
                        matrix[k][v] = '0'
                        zero.add((k, v))
    if len(zero) == 0:
        break
    for i in range(N-1, -1, -1):
        for j in range(10):
            if matrix[i][j] == '0':
                x = i - 1
                while x >= 0 and matrix[x][j] == '0':
                    x -= 1
                if x < 0:
                    matrix[i][j] = '0'
                else:
                    matrix[i][j] = matrix[x][j]
                    matrix[x][j] = '0'
for i in matrix:
    print(''.join(i))