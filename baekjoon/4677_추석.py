dx, dy = [0,0,1,-1,-1,1,1,-1], [1,-1,0,0,1,1,-1,-1]
from collections import deque
import sys
input = sys.stdin.readline
while True:
    N, M = map(int, input().split())
    if N == 0 and M == 0:
        break
    matrix = [list(input()) for _ in range(N)]
    visited = [[False] * M for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == '@' and not visited[i][j]:
                cnt += 1
                start = deque()
                start.append((i, j))
                visited[i][j] = True
                while start:
                    x, y = start.popleft()
                    for k in range(8):
                        nx, ny = x + dx[k], y + dy[k]
                        if 0 <= nx < N and 0 <= ny < M:
                            if matrix[nx][ny] == '@' and not visited[nx][ny]:
                                visited[nx][ny] = True
                                start.append((nx, ny))
    print(cnt)