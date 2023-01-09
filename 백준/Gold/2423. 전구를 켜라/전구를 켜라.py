from heapq import heappop,heappush
import sys
INF = sys.maxsize
input = sys.stdin.readline
N, M = map(int, input().split())
matrix = [[[] for _ in range(M+1)] for _ in range(N+1)]
for i in range(N):
    temp = list(input().strip())
    for j in range(M):
        if temp[j] == '/':
            matrix[i][j+1].append((0, i+1, j))
            matrix[i+1][j].append((0, i, j+1))
            matrix[i][j].append((1, i+1, j+1))
            matrix[i+1][j+1].append((1, i, j))
        else:
            matrix[i][j].append((0, i+1, j+1))
            matrix[i+1][j+1].append((0, i, j))
            matrix[i][j+1].append((1, i+1, j))
            matrix[i+1][j].append((1, i, j+1))
visited = [[INF] * (M+1) for _ in range(N+1)]
visited[0][0] = 0
start = []
heappush(start, (0, 0, 0))
while start:
    cost, x, y = heappop(start)
    if cost > visited[x][y]:
        continue
    for nc, nx, ny in matrix[x][y]:
        new_cost = cost + nc
        if visited[nx][ny] > new_cost:
            visited[nx][ny] = new_cost
            heappush(start, (new_cost, nx, ny))
print(visited[N][M] if visited[N][M] != INF else "NO SOLUTION")