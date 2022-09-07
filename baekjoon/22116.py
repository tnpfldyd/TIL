from heapq import heappop, heappush
import sys
input = sys.stdin.readline
N= int(input())
visited = [[99999999] * N for _ in range(N)]
matrix = [list(map(int, input().rstrip().split())) for _ in range(N)]
start = []
heappush(start, [0, 0, 0])
dx, dy = [0,0,1,-1], [1,-1,0,0]
while start:
    ex, x, y = heappop(start)
    if visited[x][y] != 99999999:
        continue
    if x == N-1 and y == N-1:
        print(ex)
        break
    visited[x][y] = ex
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < N:
            if visited[nx][ny] != 99999999:
                continue
            heappush(start, [max(abs(matrix[x][y]-matrix[nx][ny]), ex), nx, ny])
        