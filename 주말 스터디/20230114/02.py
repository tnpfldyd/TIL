from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
matrix = [list(map(int, input().strip().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
dx, dy = [0,0,1,-1], [1,-1,0,0]
cnt = 0
for i in range(N):
    for j in range(M):
        if not matrix[i][j] and not visited[i][j]:
            visited[i][j] = True
            start = deque()
            start.append((i, j))
            while start:
                x, y = start.popleft()
                for k in range(4):
                    nx, ny = x + dx[k], y + dy[k]
                    if not (0 <= nx < N and 0 <= ny < M):
                        if nx < 0:
                            nx = N - 1
                        elif ny < 0:
                            ny = M - 1
                        elif nx >= N:
                            nx = 0
                        else:
                            ny = 0
                    if not matrix[nx][ny] and not visited[nx][ny]:
                        visited[nx][ny] = True
                        start.append((nx, ny))
            cnt += 1
print(cnt)