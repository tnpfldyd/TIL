from collections import deque
import sys
input = sys.stdin.readline
N, M, K = map(int, input().split())
matrix = [list(input().strip()) for _ in range(N)]
visited = [[-1] * M for _ in range(N)]
dx, dy = [0,0,1,-1], [1,-1,0,0]
sx,sy,ex,ey = map(lambda x : int(x) - 1, input().split())
stack = deque()
stack.append((sx, sy))
visited[sx][sy] = 0
while stack:
    x, y = stack.popleft()
    if (x, y) == (ex, ey):
        print(visited[x][y])
        break
    for i in range(4):
        for j in range(1, K + 1):
            nx, ny = x + dx[i] * j, y + dy[i] * j
            if not (0 <= nx < N and 0 <= ny < M) or matrix[nx][ny] == '#' or (visited[nx][ny] != -1 and visited[nx][ny] < visited[x][y] + 1):
                break
            if visited[nx][ny] == -1:
                visited[nx][ny] = visited[x][y] + 1
                stack.append((nx, ny))
else:
    print(-1)