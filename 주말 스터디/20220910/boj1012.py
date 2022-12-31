from collections import deque
import sys
input = sys.stdin.readline
T = int(input())
for i in range(T):
    N, M, K = map(int, input().split())
    matrix = [[0] * M for _ in range(N)]
    for j in range(K):
        a, b = map(int, input().split())
        matrix[a][b] = 1
    dx, dy = [1,-1,0,0],[0,0,1,-1]
    cnt = 0
    visited = [[False] * M for _ in range(N)]
    for x in range(N):
        for y in range(M):
            if matrix[x][y] == 1 and not visited[x][y]:
                start = deque()
                start.append((x, y))
                visited[x][y] = True
                cnt += 1
                while start:
                    ix, iy = start.popleft()
                    for k in range(4):
                        nx = ix + dx[k]; ny = iy + dy[k]
                        if 0 <= nx < N and 0 <= ny < M:
                            if matrix[nx][ny] == 1 and not visited[nx][ny]:
                                visited[nx][ny] = True
                                start.append((nx, ny))
    print(cnt)