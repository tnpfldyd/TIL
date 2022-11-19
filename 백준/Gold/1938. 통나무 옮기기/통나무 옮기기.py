from collections import deque
import sys
input = sys.stdin.readline
N = int(input())
matrix = [list(input().strip()) for _ in range(N)]
wood = []
end = []
for i in range(N):
    for j in range(N):
        if matrix[i][j] == 'B':
            wood.append((i, j))
        elif matrix[i][j] == 'E':
            end.append((i, j))
start = deque()
if wood[1][1] - wood[0][1] == 0:
    start.append((wood[1][0], wood[1][1], 0))
else:
    start.append((wood[1][0], wood[1][1], 1))
# 0 세로 1 가로
if end[1][1] - end[0][1] == 0:
    ex, ey, edir = end[1][0], end[1][1], 0
else:
    ex, ey, edir = end[1][0], end[1][1], 1
dx, dy = [0,0,1,-1,1,1,-1,-1], [1,-1,0,0,1,-1,-1,1]
visited = [[[-1] * 2 for _ in range(N)] for _ in range(N)]
visited[start[0][0]][start[0][1]][start[0][2]] = 0
while start:
    x, y, dir = start.popleft()
    if x == ex and y == ey and dir == edir:
        print(visited[x][y][dir])
        break
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if not dir:
            if 0 <= nx < N and 0 <= ny < N and 0 <= nx-1 < N and 0 <= nx+1 < N:
                if matrix[nx][ny] != '1' and matrix[nx-1][ny] != '1' and matrix[nx+1][ny] != '1' and visited[nx][ny][dir] == -1:
                    visited[nx][ny][dir] = visited[x][y][dir] + 1
                    start.append((nx, ny, dir))
        else:
            if 0 <= nx < N and 0 <= ny < N and 0 <= ny-1 < N and 0 <= ny+1 < N:
                if matrix[nx][ny] != '1' and matrix[nx][ny-1] != '1' and matrix[nx][ny+1] != '1' and visited[nx][ny][dir] == -1:
                    visited[nx][ny][dir] = visited[x][y][dir] + 1
                    start.append((nx, ny, dir))
    if visited[x][y][abs(dir-1)] == -1:
        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if matrix[nx][ny] != '1':
                    continue
                else:
                    break
            else:
                break
        else:
            visited[x][y][abs(dir-1)] = visited[x][y][dir] + 1
            start.append((x, y, abs(dir-1)))
else:
    print(0)