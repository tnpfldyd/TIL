import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
start_x, start_y = map(int, input().split())

targets = []
for _ in range(M):
    a, b = map(int, input().split())
    targets.append((a, b))

dx = [-2, -2, -1, -1, 1, 1, 2, 2]
dy = [-1, 1, -2, 2, -2, 2, -1, 1]

dist = [[-1] * (N + 1) for _ in range(N + 1)]
dist[start_x][start_y] = 0

queue = deque([(start_x, start_y)])

while queue:
    x, y = queue.popleft()

    for i in range(8):
        nx, ny = x + dx[i], y + dy[i]

        if 1 <= nx <= N and 1 <= ny <= N and dist[nx][ny] == -1:
            dist[nx][ny] = dist[x][y] + 1
            queue.append((nx, ny))

print(' '.join(str(dist[a][b]) for a, b in targets))
