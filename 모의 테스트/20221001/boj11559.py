from collections import deque
import sys
input = sys.stdin.readline
matrix = [list(input().rstrip()) for _ in range(12)]
dx, dy = [0,0,1,-1], [1,-1,0,0]
cnt = 0
while True:
    visited = [[False] * 6 for _ in range(12)]
    zero = set()
    for i in range(12):
        for j in range(6):
            if not visited[i][j] and matrix[i][j] != '.' and matrix[i][j] != 0:
                start = deque()
                temp = []
                visited[i][j] = True
                start.append((i, j))
                temp.append((i, j))
                while start:
                    x, y = start.popleft()
                    for k in range(4):
                        nx, ny = x + dx[k], y + dy[k]
                        if 0 <= nx < 12 and 0 <= ny < 6:
                            if matrix[nx][ny] == matrix[i][j] and not visited[nx][ny]:
                                visited[nx][ny] = True
                                start.append((nx, ny))
                                temp.append((nx, ny))
                if len(temp) > 3:
                    for k, v in temp:
                        matrix[k][v] = 0
                        zero.add((k, v))
    if len(zero) == 0:
        break
    for i in range(11, -1, -1):
        for j in range(6):
            if matrix[i][j] == 0:
                x = i - 1
                while x >= 0 and matrix[x][j] == 0:
                    x -= 1
                if x < 0:
                    matrix[i][j] = 0
                else:
                    matrix[i][j] = matrix[x][j]
                    matrix[x][j] = 0
    cnt += 1
print(cnt)