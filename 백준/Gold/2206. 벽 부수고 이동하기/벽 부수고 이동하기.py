from collections import deque
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
matrix = [list(input().strip()) for _ in range(N)]
visited = [[[0] * M for _ in range(N)] for _ in range(2)]
visited[0][0][0] = 1
start = deque()
start.append((0, 0, 0))
dx, dy = [0,0,1,-1], [1,-1,0,0]
while start:
    x, y, wall = start.popleft()
    if x == N-1 and y == M-1:
        print(visited[wall][x][y])
        break
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if matrix[nx][ny] == '0' and not visited[wall][nx][ny]:
                visited[wall][nx][ny] = visited[wall][x][y] + 1
                start.append((nx, ny, wall))
            elif matrix[nx][ny] == '1' and not wall and not visited[wall+1][nx][ny]:
                visited[wall+1][nx][ny] = visited[wall][x][y] + 1
                start.append((nx, ny, wall+1))
else:
    print(-1)