from heapq import heappop, heappush
import sys
input = sys.stdin.readline
INF = sys.maxsize
M, N = map(int,input().split())
matrix = [list(input().strip()) for _ in range(N)]
visited = [[[INF] * 4 for _ in range(M)] for _ in range(N)]
s = []
for i in range(N):
    for j in range(M):
        if matrix[i][j] == 'C':
            s.append((i, j))
start = []
dx, dy = [0,-1,0,1],[1,0,-1,0]
for i in range(4):
    heappush(start, [0, i, s[0][0], s[0][1]])
    visited[s[0][0]][s[0][1]][i] = 0
while start:
    l, k, x, y = heappop(start)
    if x == s[1][0] and y == s[1][1]:
        print(l)
        break
    for i in range(4):
        if k + 2 % 4 != i:
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if i != k and matrix[nx][ny] != '*':
                    if visited[nx][ny][i] > visited[x][y][k] + 1:
                        visited[nx][ny][i] = visited[x][y][k] + 1
                        heappush(start, [l+1, i, nx, ny])
                elif i == k and matrix[nx][ny] != '*':
                    if visited[nx][ny][i] > visited[x][y][k]:
                        visited[nx][ny][i] = visited[x][y][k]
                        heappush(start, [l, i, nx, ny])