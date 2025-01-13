from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
matrix = [list(map(int, list(input().strip()))) for _ in range(N)]
q = deque()
visited = [[False] * M for _ in range(N)]
for i in range(M):
    cur = matrix[0][i]
    if not cur:
        q.append((0, i))
        visited[0][i] = True

dx, dy = [0, 0, -1, 1], [1, -1, 0, 0]
while q:
    x, y = q.popleft()
    if x == N - 1:
        print("YES")
        break
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if not visited[nx][ny] and not matrix[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny))
else:
    print("NO")