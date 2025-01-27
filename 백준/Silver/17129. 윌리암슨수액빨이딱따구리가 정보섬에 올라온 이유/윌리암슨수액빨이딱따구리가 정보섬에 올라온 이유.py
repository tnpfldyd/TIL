from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
matrix = []
sx, sy = 0, 0
q = deque()
visited = [[False] * M for _ in range(N)]
for i in range(N):
    row = list(input().strip())
    for j in range(M):
        if row[j] == '2':
            sx, sy = i, j
            q.append((i, j, 0))
            visited[i][j] = True
    matrix.append(row)

dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
result = 0
while q:
    x, y, cnt = q.popleft()
    if result:
        print("TAK")
        print(result)
        break
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and matrix[nx][ny] != '1':
            visited[nx][ny] = True
            q.append((nx, ny, cnt + 1))
            if matrix[nx][ny] != '0':
                result = cnt + 1
else:
    print("NIE")