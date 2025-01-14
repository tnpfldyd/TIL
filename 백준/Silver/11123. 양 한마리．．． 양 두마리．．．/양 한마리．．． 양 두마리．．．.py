from collections import deque
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    N, M = map(int, input().split())
    grid = [list(input().strip()) for _ in range(N)]
    visited = [[False] * M for _ in range(N)]
    result = 0
    for i in range(N):
        for j in range(M):
            if grid[i][j] == '.' or visited[i][j]:
                continue
            visited[i][j] = True
            q = deque()
            q.append((i, j))
            dx, dy = [0, 0, -1, 1] , [1, -1, 0, 0]
            while q:
                x, y = q.popleft()
                for k in range(4):
                    nx, ny = x + dx[k], y + dy[k]
                    if not (0 <= nx < N and 0 <= ny < M):
                        continue
                    if visited[nx][ny] or grid[nx][ny] == '.':
                        continue
                    visited[nx][ny] = True
                    q.append((nx, ny))
            result += 1
    print(result)