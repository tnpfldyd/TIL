import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

sharks = []
space = []
for i in range(N):
    row = list(map(int, input().split()))
    space.append(row)
    for j in range(M):
        if row[j] == 1:
            sharks.append((i, j))

queue = deque(sharks)
distance = [[-1] * M for _ in range(N)]

for r, c in sharks:
    distance[r][c] = 0

directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

while queue:
    r, c = queue.popleft()
    
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if 0 <= nr < N and 0 <= nc < M and distance[nr][nc] == -1:
            distance[nr][nc] = distance[r][c] + 1
            queue.append((nr, nc))

max_distance = 0
for i in range(N):
    for j in range(M):
        max_distance = max(max_distance, distance[i][j])

print(max_distance)