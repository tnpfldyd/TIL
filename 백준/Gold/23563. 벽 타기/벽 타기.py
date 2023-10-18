from heapq import heappop, heappush
import sys
input = sys.stdin.readline
INF = sys.maxsize
H, W = map(int, input().split())
matrix = [list(input().rstrip()) for _ in range(H)]
visited = [[INF] * W for _ in range(H)]
sx, sy = 0, 0
ex, ey = 0, 0
for i in range(H):
    for j in range(W):
        if matrix[i][j] == 'S':
            sx, sy = i, j
        elif matrix[i][j] == 'E':
            ex, ey = i, j
visited[sx][sy] = 0
pq = []
heappush(pq, (0, sx, sy))
dx, dy = [0,0,1,-1], [1,-1,0,0]
def check(x, y):
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < H and 0 <= ny < W and matrix[nx][ny] == '#':
            return True
    return False
while pq:
    cost, x, y = heappop(pq)
    if x == ex and y == ey:
        print(cost)
        break
    if visited[x][y] < cost:
        continue
    curFlag = check(x, y)
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < H and 0 <= ny < W and matrix[nx][ny] != '#':
            nextFlag = check(nx, ny)
            if curFlag and nextFlag:
                if visited[nx][ny] > cost:
                    visited[nx][ny] = cost
                    heappush(pq, (cost, nx, ny))
            else:
                if visited[nx][ny] > cost + 1:
                    visited[nx][ny] = cost + 1
                    heappush(pq, (cost + 1, nx, ny))