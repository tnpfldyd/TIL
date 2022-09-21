from pprint import pprint
from heapq import heappop, heappush
import sys
input = sys.stdin.readline
INF = sys.maxsize
H, W = map(int, input().split())
matrix = [list(input().rstrip()) for _ in range(H)]
visited = [[INF] * W for _ in range(H)]
s1, s2 = 0, 0
e1, e2 = 0, 0
for i in range(H):
    for j in range(W):
        if matrix[i][j] == 'S':
            s1, s2 = i, j
        elif matrix[i][j] == 'E':
            e1, e2 = i, j
visited[s1][s2] = 0
start = []
heappush(start, [0, s1, s2])
dx, dy = [0,0,1,-1], [1,-1,0,0]
while start:
    z, x, y = heappop(start)
    if x == e1 and y == e2:
        print(z)
        break
    cnt = 0
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < H and 0 <= ny < W:
            if matrix[nx][ny] == '#':
                cnt += 1
    if cnt > 0:
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            cntt = 0
            if 0 <= nx < H and 0 <= ny < W:
                for l in range(4):
                    sx, sy = nx + dx[k], ny + dy[k]
                    if 0 <= sx < H and 0 <= sy < W:
                        if matrix[sx][sy] == '#':
                            cntt += 1
            if cntt > 0 and matrix[nx][ny] != '#':
                if visited[nx][ny] > visited[x][y]:
                    visited[nx][ny] = visited[x][y]
                    heappush(start, [z, nx, ny])
            else:
                if 0 <= nx < H and 0 <= ny < W and matrix[nx][ny] != '#':
                    if visited[nx][ny] > visited[x][y] + 1:
                        visited[nx][ny] = visited[x][y] + 1
                        heappush(start, [z+1, nx, ny])
    else:
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < H and 0 <= ny < W and matrix[nx][ny] != '#':
                if visited[nx][ny] > visited[x][y] + 1:
                    visited[nx][ny] = visited[x][y] + 1
                    heappush(start, [z+1, nx, ny])
print(visited)