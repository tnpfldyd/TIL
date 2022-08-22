from collections import deque
import sys
input = sys.stdin.readline
N = int(input())
matrix = [list(input().rstrip()) for _ in range(N)]
Rvisited = [[False] * N for _ in range(N)]
ivisited = [[False] * N for _ in range(N)]
dx, dy = [0,0,1,-1],[1,-1,0,0]
Rcnt, icnt = 0, 0
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
        if not ivisited[x][y]:
            start = deque()
            start.append((x, y))
            ivisited[x][y] = True
            while start:
                a, b = start.popleft()
                for k in range(4):
                    nx = a + dx[k]; ny = b + dy[k]
                    if 0 <= nx < N and 0 <= ny < N and not ivisited[nx][ny]:
                        if matrix[x][y] == matrix[nx][ny]:
                            start.append((nx, ny))
                            ivisited[nx][ny] = True
            icnt += 1
print(icnt, Rcnt)