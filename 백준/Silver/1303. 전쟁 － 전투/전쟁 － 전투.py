from collections import deque
import sys
input = sys.stdin.readline
W, B = 0, 0
M, N = map(int, input().split())
matrix = [list(input().rstrip()) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
dx, dy = [0,0,1,-1], [1,-1,0,0]
for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            visited[i][j] = True
            cnt = 1
            start = deque()
            start.append((i, j))
            while start:
                x, y = start.popleft()
                for k in range(4):
                    nx, ny = x + dx[k], y + dy[k]
                    if 0 <= nx < N and 0 <= ny < M:
                        if matrix[nx][ny] == matrix[i][j] and not visited[nx][ny]:
                            cnt += 1
                            visited[nx][ny] = True
                            start.append((nx, ny))
            if matrix[i][j] == 'W':
                W += cnt**2
            else:
                B += cnt**2
print(W, B)