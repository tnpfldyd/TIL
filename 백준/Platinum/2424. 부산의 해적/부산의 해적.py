from collections import deque
import sys
input = sys.stdin.readline
INF = sys.maxsize

N, M = map(int, input().split())
matrix = []
sx, sy, ex, ey, hx, hy = 0, 0, 0, 0, 0, 0
busan_dist = []
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
for i in range(N):
    row = list(input().strip())
    for j in range(M):
        if row[j] == 'Y':
            sx, sy = i, j
            row[j] = '.'
        elif row[j] == 'V':
            hx, hy = i, j
            row[j] = '.'
        elif row[j] == 'T':
            ex, ey = i, j
            row[j] = '.'
    matrix.append(row)
    busan_dist.append([INF] * M)

busanQ = deque()
busanQ.append((hx, hy))
busan_dist[hx][hy] = 0

while busanQ:
    x, y = busanQ.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if matrix[nx][ny] == '.' and busan_dist[nx][ny] > busan_dist[x][y] + 1:
                busan_dist[nx][ny] = busan_dist[x][y] + 1
                busanQ.append((nx, ny))

busan_matrix = [[-1] * M for _ in range(N)] 

for i in range(N):
    value = INF
    for j in range(M):
        if matrix[i][j] == 'I':
            value = INF
            busan_matrix[i][j] = INF
            continue
        value = min(value, busan_dist[i][j])
        busan_matrix[i][j] = value
    value = INF
    for j in range(M - 1, -1, -1):
        if matrix[i][j] == 'I':
            value = INF
            busan_matrix[i][j] = INF
            continue
        value = min(value, busan_dist[i][j])
        busan_matrix[i][j] = min(value, busan_matrix[i][j])

for j in range(M):
    value = INF
    for i in range(N):
        if matrix[i][j] == 'I':
            value = INF
            busan_matrix[i][j] = INF
            continue
        value = min(value, busan_dist[i][j])
        busan_matrix[i][j] = min(value, busan_matrix[i][j])
    value = INF
    for i in range(N - 1, -1, -1):
        if matrix[i][j] == 'I':
            value = INF
            busan_matrix[i][j] = INF
            continue
        value = min(value, busan_dist[i][j])
        busan_matrix[i][j] = min(value, busan_matrix[i][j])
   

visited = [[False] * M for _ in range(N)]
suaQ = deque()
suaQ.append((sx, sy, 0))
visited[sx][sy] = True
while suaQ:
    x, y, cnt = suaQ.popleft()
    if (x, y) == (ex, ey):
        print('YES')
        break
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if matrix[nx][ny] == '.' and not visited[nx][ny] and busan_matrix[nx][ny] > cnt + 1:
                visited[nx][ny] = True
                suaQ.append((nx, ny, cnt + 1))
else:
    print('NO')
