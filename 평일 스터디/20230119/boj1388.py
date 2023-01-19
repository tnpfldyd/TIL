import sys
input = sys.stdin.readline
N, M = map(int, input().split())
matrix = [list(input().strip()) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

cnt = 0
for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            visited[i][j] = True
            start = []
            if matrix[i][j] == '-':
                start.append((i, j, 0, 1))
            else:
                start.append((i, j, 1, 0))
            while start:
                x, y, dx, dy = start.pop()
                nx, ny = x + dx, y + dy
                if 0 <= nx < N and 0 <= ny < M:
                    if matrix[nx][ny] == matrix[x][y] and not visited[nx][ny]:
                        visited[nx][ny] = True
                        start.append((nx, ny, dx, dy))
            cnt += 1
print(cnt)