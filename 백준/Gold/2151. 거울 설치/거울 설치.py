from heapq import heappop, heappush
import sys
input = sys.stdin.readline
INF = sys.maxsize
N = int(input())
matrix = [list(input().strip()) for _ in range(N)]
visited = [[[INF] * 4 for _ in range(N)] for _ in range(N)]
s = []
for i in range(N):
    for j in range(N):
        if matrix[i][j] == '#':
            s.append((i, j))
start = []
dx, dy = [0,0,1,-1],[1,-1,0,0]
for i in range(4):
    heappush(start, [0, i, s[0][0], s[0][1]])
    visited[s[0][0]][s[0][1]][i] = 0
while start:
    l, k, x, y = heappop(start)
    if x == s[1][0] and y == s[1][1]:
        print(l)
        break
    nx, ny = x + dx[k], y + dy[k]
    if 0 <= nx < N and 0 <= ny < N:
        if matrix[nx][ny] != '*':
            if matrix[nx][ny] == '!':
                if k > 1:
                    for i in range(2):
                        if visited[nx][ny][i] > visited[x][y][k] + 1:
                            visited[nx][ny][i] = visited[x][y][k] + 1
                            heappush(start, [l+1, i, nx, ny])
                else:
                    for i in range(2, 4):
                        if visited[nx][ny][i] > visited[x][y][k] + 1:
                            visited[nx][ny][i] = visited[x][y][k] + 1
                            heappush(start, [l+1, i, nx, ny])
            if visited[nx][ny][k] > visited[x][y][k]:
                visited[nx][ny][k] = visited[x][y][k]
                heappush(start, [l, k, nx, ny])