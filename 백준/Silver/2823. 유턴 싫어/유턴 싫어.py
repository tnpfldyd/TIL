from collections import deque
import sys
input = sys.stdin.readline

R, C = map(int, input().split())
grid = []
start = []
for i in range(R):
    row = list(input().strip())
    grid.append(row)
    if len(start) == 0:
        for j in range(C):
            if row[j] == '.':
                start = [i, j]

def bfs(r, c):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited = [[False] * C for _ in range(R)]
    queue = deque([(r, c)])
    visited[r][c] = True

    while queue:
        x, y = queue.popleft()
        cnt = 0
        for dr, dc in directions:
            nr, nc = x + dr, y + dc
            if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] == '.':
                cnt += 1
                if not visited[nr][nc]:
                    visited[nr][nc] = True
                    queue.append((nr, nc))
        if cnt < 2:
            return 1
    return 0

print(bfs(start[0], start[1]))