from collections import deque
import sys
input = sys.stdin.readline
K = int(input())
N, M = map(int, input().split())
matrix = [list(map(int, input().rstrip().split())) for _ in range(M)]
visited = [[[-1] * (K+1) for _ in range(N)] for _ in range(M)]
visited[0][0][0] = 0
start = deque()
start.append((0, 0, 0))
dx, dy = [0,0,-1,1], [-1,1,0,0]
sx, sy = [2,1,2,1,-1,-2,-2,-1],[1,2,-1,-2,-2,-1,1,2]
while start:
    x, y, k = start.popleft()
    if x == M-1 and y == N-1:
        print(visited[x][y][k])
        break
    if k < K:
        for i in range(8):
            nx, ny = x + sx[i], y + sy[i]
            if 0 <= nx < M and 0 <= ny < N:
                if visited[nx][ny][k+1] == -1 and matrix[nx][ny] == 0:
                    visited[nx][ny][k+1] = visited[x][y][k] + 1
                    start.append((nx, ny, k+1))
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < M and 0 <= ny < N:
            if visited[nx][ny][k] == -1 and matrix[nx][ny] == 0:
                visited[nx][ny][k] = visited[x][y][k] + 1
                start.append((nx, ny, k))
else:
    print(-1)