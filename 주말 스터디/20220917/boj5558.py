from collections import deque
import sys
input = sys.stdin.readline
N, M, K = map(int, input().split())
matrix = [list(input().rstrip()) for _ in range(N)]
visited = [[[-1] * (K+1) for _ in range(M)] for _ in range(N)]
start = deque()
a, b = 0, 0
for i in range(N):
    for j in range(M):
        if matrix[i][j] == 'S':
            start.append((i, j, 0))
            visited[i][j][0] = 0
        elif matrix[i][j] == str(K):
            a, b = i, j
target = 1
dx, dy = [0,0,1,-1],[1,-1,0,0]
while start:
    x, y, z = start.popleft()
    if x == a and y == b and z == K:
        print(visited[x][y][z])
        break
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < M and visited[nx][ny][z] == -1:
            if matrix[nx][ny] != 'X' and matrix[nx][ny] != str(target):
                visited[nx][ny][z] = visited[x][y][z] + 1
                start.append((nx, ny, z))
            elif matrix[nx][ny] == str(target) and z+1 == target:
                target += 1
                visited[nx][ny][z+1] = visited[x][y][z] + 1 
                start.append((nx, ny, z+1))
print(visited)