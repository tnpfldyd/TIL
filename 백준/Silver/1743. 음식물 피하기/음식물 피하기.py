from collections import deque
import sys
input = sys.stdin.readline
N, M, T = map(int, input().split())
matrix = [['.'] * M for _ in range(N)]
dx, dy = [0,0,1,-1], [1,-1,0,0]
for i in range(T):
    a, b = map(int, input().split())
    a -= 1; b -= 1
    matrix[a][b] = '#'
visited = [[False] * M for _ in range(N)]
max_cnt = 0
for i in range(N):
    for j in range(M):
        if matrix[i][j] == '#' and not visited[i][j]:
            start = deque()
            cnt = 1
            start.append((i, j))
            visited[i][j] = True
            while start:
                x, y = start.popleft()
                for k in range(4):
                    nx, ny = x + dx[k], y + dy[k]
                    if 0 <= nx < N and 0 <= ny < M:
                        if matrix[nx][ny] == '#' and not visited[nx][ny]:
                            cnt += 1
                            visited[nx][ny] = True
                            start.append((nx, ny))
            if cnt > max_cnt:
                max_cnt = cnt
print(max_cnt)