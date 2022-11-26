from heapq import heappop, heappush
import sys
input = sys.stdin.readline
INF = sys.maxsize
N, M = map(int, input().split())
matrix = [list(map(int, input().strip().split())) for _ in range(N)]
visited = [[[INF] * 2 for _ in range(M)] for _ in range(N)]
visited[0][0][0] = matrix[0][0]
start = []
start.append((matrix[0][0], 0, 0, 0))
dx, dy = [0,0,1,-1], [1,-1,0,0]
while start:
    level, x, y, cnt = heappop(start)
    temp = visited[x][y][cnt]
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            next_level = max(matrix[nx][ny], temp)
            if visited[nx][ny][cnt] > next_level:
                visited[nx][ny][cnt] = next_level
                heappush(start, (next_level, nx, ny, cnt))
        if not cnt:
            nx, ny = nx + dx[i], ny + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                next_level = max(matrix[nx][ny], temp)
                if visited[nx][ny][cnt+1] > next_level:
                    visited[nx][ny][cnt+1] = next_level
                    heappush(start, (next_level, nx, ny, cnt+1))
print(min(visited[N-1][M-1]))