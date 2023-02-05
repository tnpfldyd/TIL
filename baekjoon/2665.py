from heapq import heappop, heappush
import sys
input = sys.stdin.readline
INF = sys.maxsize
N = int(input())
matrix = [list(map(int,input().rstrip())) for _ in range(N)]
visited = [[INF]*N for _ in range(N)]
start = []
heappush(start, (0, 0, 0))
visited[0][0] = 0
dx, dy = [0,0,1,-1], [1,-1,0,0]
while start:
    white, x, y = heappop(start)
    if (x, y) == (N-1, N-1):
        print(white)
        break
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < N:
            if not matrix[nx][ny]:
                next_cost = white + 1
            else:
                next_cost = white
            if visited[nx][ny] > next_cost:
                visited[nx][ny] = next_cost
                heappush(start, (next_cost, nx, ny))
