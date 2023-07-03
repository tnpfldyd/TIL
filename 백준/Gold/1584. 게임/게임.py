from heapq import heappop, heappush
import sys
input = sys.stdin.readline
INF = sys.maxsize
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]

matrix = [[0] * 501 for _ in range(501)]
visited = [[INF] * 501 for _ in range(501)]

def setMatrix(x):
    N = int(input())
    for _ in range(N):
        x1, y1, x2, y2 = map(int, input().split())
        if x1 > x2:
            x1, x2 = x2, x1
        if y1 > y2:
            y1, y2 = y2, y1
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                matrix[i][j] = x

setMatrix(1), setMatrix(-1)

pq = []
heappush(pq, (0, 0, 0))
visited[0][0] = 0

while pq:
    cost, x, y = heappop(pq)
    if visited[x][y] < cost:
        continue
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < 501 and 0 <= ny < 501:
            if matrix[nx][ny] != -1:
                nc = matrix[nx][ny] + cost
                if visited[nx][ny] > nc:
                    visited[nx][ny] = nc
                    heappush(pq, (nc, nx, ny))

print(visited[500][500] if visited[500][500] != INF else -1)