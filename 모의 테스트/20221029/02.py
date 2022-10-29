# 불지르고 피하기
board = [[0,0,1,0,0,0],[0,2,0,0,0,1],[0,0,2,1,0,0],[0,0,0,0,0,0],[0,0,0,0,1,0],[0,1,0,0,0,0]]
k = 2
ax = 1; ay = 2
from collections import deque
dx, dy = [0,0,1,-1], [1,-1,0,0]
N = len(board)
for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
            for l in range(4):
                nx, ny = i + dx[l], j + dy[l]
                cnt = 0
                while 0 <= nx < N and 0 <= ny < N and cnt < k and (board[nx][ny] == 0 or board[nx][ny] == 3):
                    board[nx][ny] = 3
                    nx, ny = nx + dx[l], ny + dy[l]
                    cnt += 1
start = deque()
start.append((ax, ay))

visited = [[-1] * N for _ in range(N)]
visited[ax][ay] = 0
while start:
    x, y = start.popleft()
    if board[x][y] == 0:
        print(visited[x][y])
        break
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < N and 0 <= ny < N:
            if board[nx][ny] != 1 and board[nx][ny] != 2 and visited[nx][ny] == -1:
                visited[nx][ny] = visited[x][y] + 1
                start.append((nx, ny))
else:
    print(-1)