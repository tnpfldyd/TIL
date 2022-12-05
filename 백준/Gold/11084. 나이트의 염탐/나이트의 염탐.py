from collections import deque
INF = 1000000009
N, M = map(int, input().split())
visited = [[-1] * M for _ in range(N)]
dp = [[0] * M for _ in range(N)]
visited[0][0] = 0
dp[0][0] = 1
start = deque()
dx, dy = [1,2,2,1,-1,-2,-2,-1], [2,1,-1,-2,-2,-1,1,2]
start.append((0, 0))
while start:
    x, y = start.popleft()
    for i in range(8):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if visited[nx][ny] == visited[x][y] + 1 or visited[nx][ny] == -1:
                dp[nx][ny] = (dp[nx][ny] + dp[x][y]) % INF
                if visited[nx][ny] == -1:
                    visited[nx][ny] = visited[x][y] + 1
                    start.append((nx, ny))
if visited[N-1][M-1] == -1:
    print('None')
else:
    print(visited[N-1][M-1], dp[N-1][M-1])