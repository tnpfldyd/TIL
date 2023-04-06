from heapq import heappop, heappush
import sys
input = sys.stdin.readline
INF = sys.maxsize
matrix = []
N, M = map(int, input().split())
for i in range(N):
    arr = list(map(int, input().split()))
    for j in range(M):
        if arr[j] == -2:
            arr[j] = 0
    matrix.append(arr)

stack = []
visited = [[INF] * M for _ in range(N)]
for i in range(N):
    if matrix[i][M - 1] == -1:
        continue
    heappush(stack, (matrix[i][M - 1], i, M - 1))
    visited[i][M - 1] = matrix[i][M - 1]
for i in range(M):
    if matrix[0][i] == -1:
        continue
    heappush(stack, (matrix[0][i], 0, i))
    visited[0][i] = matrix[0][i]
dx, dy = [0,0,1,-1,1,1,-1,-1],[1,-1,0,0,-1,1,-1,1]
while stack:
    cost, x, y = heappop(stack)
    if visited[x][y] < cost:
        continue
    for i in range(8):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if matrix[nx][ny] != -1:
                nxt_cost = cost + matrix[nx][ny]
                if visited[nx][ny] > nxt_cost:
                    visited[nx][ny] = nxt_cost
                    heappush(stack, (nxt_cost, nx, ny))
answer = INF
for i in range(N):
    answer = min(answer, visited[i][0])
for i in range(M):
    answer = min(answer, visited[N - 1][i])
print(answer if answer != INF else -1)