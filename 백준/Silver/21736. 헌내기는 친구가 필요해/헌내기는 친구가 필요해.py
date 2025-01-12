from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
matrix = []
sx, sy = 0, 0
for i in range(N):
    row = list(input().strip())
    for j in range(M):
        if row[j] == 'I':
            sx, sy = i, j
    matrix.append(row)         
visited = [[False] * M for _ in range(N)]
visited[sx][sy] = True
q = deque()
q.append((sx, sy))
dx, dy = [0, 0, -1, 1], [1, -1, 0, 0]
result = 0
while q:
    x, y = q.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if not visited[nx][ny] and matrix[nx][ny] != 'X':
                visited[nx][ny] = True
                q.append((nx, ny))
                if matrix[nx][ny] == 'P':
                    result += 1

print(result if result else 'TT')