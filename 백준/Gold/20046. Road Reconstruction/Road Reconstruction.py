from heapq import heappop, heappush
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
visited = [[99999999] * M for _ in range(N)]
matrix = [list(map(int, input().rstrip().split())) for _ in range(N)]
start = []
heappush(start, [matrix[0][0], 0, 0])
dx, dy = [0,0,1,-1], [1,-1,0,0]
visited[0][0] = matrix[0][0]
if matrix[0][0] == -1:
    print(-1)
    sys.exit(0)
while start:
    ex, x, y = heappop(start)
    if x == N-1 and y == M-1:
        print(visited[x][y])
        break
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if visited[nx][ny] == 99999999:
                if matrix[nx][ny] != -1:
                    new_ex = ex + matrix[nx][ny]
                    if new_ex < visited[nx][ny]:
                        visited[nx][ny] = new_ex
                        heappush(start, [new_ex, nx, ny])
else:
    print(-1)