from collections import deque
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
matrix = [list(map(int, input().rstrip().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
dx, dy = [0,0,1,-1,-1,1,1,-1], [1,-1,0,0,1,1,-1,-1]
cnt = 0
for i in range(N):
    for j in range(M):
        if matrix[i][j] == 1 and not visited[i][j]:
            start = deque()
            start.append((i, j))
            visited[i][j] = True
            while start:
                x, y = start.popleft()
                for k in range(8):
                    nx, ny = x + dx[k], y + dy[k]
                    if 0 <= nx < N and 0 <= ny < M:
                        if matrix[nx][ny] == 1 and not visited[nx][ny]:
                            visited[nx][ny] = True
                            start.append((nx, ny))
            cnt += 1
print(cnt)