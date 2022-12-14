from heapq import heappop, heappush
import sys
input = sys.stdin.readline
INF = sys.maxsize
N, T = map(int, input().split())
matrix = [list(map(int, input().strip().split())) for _ in range(N)]
dx, dy = [1, -1,  0,  0,  0,  1,  2,  3,  2,  1,  0, -1, -2, -3, -2, -1], [0,  0,  1, -1,  3,  2,  1,  0, -1, -2, -3, -2, -1,  0,  1,  2]
visited = [[INF] * N for _ in range(N)]
visited[0][0] = 0
start = []
answer = INF
heappush(start, [0, 0, 0])
while start:
    cost, x, y = heappop(start)
    if cost > visited[x][y]:
        continue
    temp = (N-x-1) + (N-y-1)
    if temp <= 2:
        answer = min(answer, cost + temp*T)
    for i in range(16):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < N:
            next_cost = cost + matrix[nx][ny] + 3*T
            if visited[nx][ny] > next_cost:
                visited[nx][ny] = next_cost
                heappush(start, [next_cost, nx, ny])
print(answer)