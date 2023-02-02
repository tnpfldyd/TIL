from heapq import heappop, heappush
import sys
input = sys.stdin.readline
INF = sys.maxsize
N, M = map(int, input().split())
matrix = [list(map(int,input().rstrip())) for _ in range(M)]
visited = [[INF] * N for _ in range(M)]
start = []
heappush(start, (0, 0, 0))
visited[0][0] = 0
dx, dy = [0,0,1,-1], [1,-1,0,0]
while start:
    cost, x, y = heappop(start)
    if x == M-1 and y == N-1:
        print(cost)
        break
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < M and 0 <= ny < N:
            if matrix[nx][ny]:
                next_cost = cost + 1
            else:
                next_cost = cost
            if visited[nx][ny] > next_cost:
                visited[nx][ny] = next_cost
                heappush(start, (next_cost, nx, ny))