from collections import deque
import sys
input = sys.stdin.readline
N, M, K= map(int,input().split())
visited = [[[0] * (K + 1) for _ in range(M)] for _ in range(N)]
matrix = [list(map(int,input().strip())) for _ in range(N)]
dx, dy = [0,0,1,-1],[1,-1,0,0]
visited[0][0][K] = 1
start = deque()
start.append((0,0,K))
while start:
    x, y, z = start.popleft()
    if x == N-1 and y == M-1:
        print(visited[x][y][z])
        break
    for i in range(4):
        nx = x + dx[i]; ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if matrix[nx][ny] == 1 and z > 0 and visited[nx][ny][z-1] == 0:
                visited[nx][ny][z-1] = visited[x][y][z] + 1
                start.append((nx, ny, z-1))
            elif matrix[nx][ny] == 0 and visited[nx][ny][z] == 0:
                visited[nx][ny][z] = visited[x][y][z] + 1
                start.append((nx, ny, z))
else:
    print(-1)