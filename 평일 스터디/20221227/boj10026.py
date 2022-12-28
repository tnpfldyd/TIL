from collections import deque
import sys
input = sys.stdin.readline
N = int(input())
matrix = [list(input().rstrip()) for _ in range(N)]
Rvisited = [[False] * N for _ in range(N)]
Lvisited = [[False] * N for _ in range(N)]
dx, dy = [0,0,1,-1],[1,-1,0,0]
Rcnt, Lcnt = 0, 0
for x in range(N):
    for y in range(N):
        if not Rvisited[x][y]:
            start = deque()
            start.append((x, y))
            Rvisited[x][y] = True
            while start:
                a, b = start.popleft()
                for k in range(4):
                    nx = a + dx[k]; ny = b + dy[k]
                    if 0 <= nx < N and 0 <= ny < N and not Rvisited[nx][ny]:
                        if matrix[x][y] == 'R' or matrix[x][y] == 'G':
                            if matrix[nx][ny] == 'R' or matrix[nx][ny] == 'G':
                                start.append((nx, ny))
                                Rvisited[nx][ny] = True
                        if matrix[x][y] == 'B' and matrix[nx][ny] == 'B':
                            start.append((nx, ny))
                            Rvisited[nx][ny] = True
            Rcnt += 1
        if not Lvisited[x][y]:
            start = deque()
            start.append((x, y))
            Lvisited[x][y] = True
            while start:
                a, b = start.popleft()
                for k in range(4):
                    nx = a + dx[k]; ny = b + dy[k]
                    if 0 <= nx < N and 0 <= ny < N and not Lvisited[nx][ny]:
                        if matrix[x][y] == matrix[nx][ny]:
                            start.append((nx, ny))
                            Lvisited[nx][ny] = True
            Lcnt += 1
print(Lcnt, Rcnt)