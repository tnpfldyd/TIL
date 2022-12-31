from collections import deque
N, M = map(int,input().split())
visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
matrix = [list(map(int,input())) for _ in range(N)]
dx, dy = [0,0,1,-1],[1,-1,0,0]
visited[0][0][0] = 1
start = deque()
start.append((0,0,0))
while start:
    x, y, z = start.popleft()
    if x == N-1 and y == M-1:
        print(visited[x][y][z])
        break
    for i in range(4):
        nx = x + dx[i]; ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M and visited[nx][ny][z] == 0:
            if matrix[nx][ny] == 0:
                visited[nx][ny][z] = visited[x][y][z] + 1
                start.append((nx, ny, z))
            elif matrix[nx][ny] == 1 and z == 0:
                visited[nx][ny][1] = visited[x][y][0] + 1
                start.append((nx, ny, 1))
else:
    print(-1)