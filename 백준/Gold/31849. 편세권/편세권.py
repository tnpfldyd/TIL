from collections import deque
import sys
input = sys.stdin.readline

N, M, R, C = map(int, input().split())
rooms = [tuple(map(int, input().split())) for _ in range(R)]
q = deque()
dist = [[-1] * M for _ in range(N)]
for _ in range(C):
    a, b = map(int, input().split())
    dist[a - 1][b - 1] = 0
    q.append((a - 1, b - 1))
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
while q:
    x, y = q.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < M and dist[nx][ny] == -1:
            dist[nx][ny] = dist[x][y] + 1
            q.append((nx, ny))
answer = sys.maxsize
for a, b, c in rooms:
    answer = min(answer, dist[a - 1][b - 1] * c)
print(answer)