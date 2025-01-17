from collections import deque
import sys
input = sys.stdin.readline
M, N = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
visited[0][0] = True
q = deque([(0, 0)])
dx, dy = [0, 1], [1, 0]
while q:
    x, y = q.popleft()
    if (x, y) == (N - 1, M - 1):
        print("Yes")
        break
    for i in range(2):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if not visited[nx][ny] and matrix[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny))
else:
    print("No")