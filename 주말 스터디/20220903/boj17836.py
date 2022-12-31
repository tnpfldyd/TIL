from collections import deque
import sys
input = sys.stdin.readline
N, M, T = map(int, input().split())
matrix = [list(map(int, input().rstrip().split())) for _ in range(N)]
visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
start = deque()
start.append((0,0,0))
dx, dy = [0,0,1,-1],[1,-1,0,0]
while start:
    x, y, z = start.popleft()
    if x == N-1 and y == M-1:
        if visited[x][y][z] <= T:
            print(visited[x][y][z])
            break
        else:
            print('Fail')
            break
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if z == 1 and visited[nx][ny][z] == 0:
                visited[nx][ny][z] = visited[x][y][z] + 1
                start.append((nx, ny, z))
            elif z == 0 and visited[nx][ny][z] == 0 and matrix[nx][ny] == 2:
                visited[nx][ny][1] = visited[x][y][z] + 1
                start.append((nx, ny, 1))
            elif z == 0 and visited[nx][ny][z] == 0 and matrix[nx][ny] == 0:
                visited[nx][ny][z] = visited[x][y][z] + 1
                start.append((nx, ny, z))
else:
    print('Fail')