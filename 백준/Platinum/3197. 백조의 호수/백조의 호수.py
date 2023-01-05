from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
matrix = [list(input().strip()) for _ in range(N)]
wv = [[False] * M for _ in range(N)]
sv = [[False] * M for _ in range(N)]
swan = []
ws, wt, ss, st = deque(), deque(), deque(), deque()
for i in range(N):
    for j in range(M):
        if matrix[i][j] == 'L':
            swan.append(i); swan.append(j)
            matrix[i][j] = '.'
        if matrix[i][j] == '.':
            ws.append((i, j))
            wv[i][j] = True
sx, sy, ex, ey = swan
ss.append((sx, sy))
sv[sx][sy] = True
cnt = 0
dx, dy = [0,0,-1,1], [-1,1,0,0]
def bfs():
    while ws:
        x, y = ws.popleft()
        matrix[x][y] = '.'
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and not wv[nx][ny]:
                wv[nx][ny] = True
                if wv[nx][ny] == '.':
                    ws.append((nx, ny))
                else:
                    wt.append((nx, ny))
    while ss:
        x, y = ss.popleft()
        if x == ex and y == ey:
            return True
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and not sv[nx][ny]:
                sv[nx][ny] = True
                if matrix[nx][ny] == '.':
                    ss.append((nx, ny))
                else:
                    st.append((nx, ny))
    return False
while True:
    if bfs():
        break
    ws, ss = wt, st
    wt, st = deque(), deque()
    cnt += 1
print(cnt)