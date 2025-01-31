from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
dx, dy = [0, 0, 1, -1, 1, 1, -1, -1], [1, -1, 0, 0, 1, -1, 1, -1]
cnt = 0
for i in range(N):
    for j in range(M):
        if matrix[i][j] and not visited[i][j]:
            q = deque([(i, j)])
            visited[i][j] = True
            while q:
                x, y = q.popleft()
                for k in range(8):
                    nx, ny = x + dx[k], y + dy[k]
                    if 0 <= nx < N and 0 <= ny < M and matrix[nx][ny] and not visited[nx][ny]:
                        visited[nx][ny] = True
                        q.append((nx, ny))
            cnt += 1

print(cnt)