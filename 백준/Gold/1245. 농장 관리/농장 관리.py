from collections import deque
import sys
input = sys.stdin.readline

dx, dy = [1, 1, 0, -1, -1, -1, 0, 1], [0, 1, 1, 1, 0, -1, -1, -1]

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
answer = 0

def bfs(i, j):
    flag = True
    q = deque()
    q.append((i, j))
    visited[i][j] = True
    
    while q:
        x, y = q.popleft()
        for d in range(8):
            nx = x + dx[d]
            ny = y + dy[d]
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue
            if board[i][j] < board[nx][ny]:
                flag = False
            if visited[nx][ny] or board[i][j] != board[nx][ny]:
                continue
            q.append((nx, ny))
            visited[nx][ny] = True
    return flag

for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            answer += bfs(i, j)
print(answer)