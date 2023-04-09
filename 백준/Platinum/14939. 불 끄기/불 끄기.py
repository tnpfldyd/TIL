import sys
input = sys.stdin.readline
INF = sys.maxsize
N = 10

matrix = [[False] * N for _ in range(N)]

dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]

def toggle(x, y):
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < N:
            tmp_matrix[nx][ny] = not tmp_matrix[nx][ny]
    tmp_matrix[x][y] = not tmp_matrix[x][y]

def init():
    for i in range(N):
        for j in range(N):
            tmp_matrix[i][j] = matrix[i][j]

def islight():
    for i in range(N):
        for j in range(N):
            if tmp_matrix[i][j]:
                return True
    return False

for i in range(N):
    line = input().rstrip()
    for j in range(N):
        if line[j] == 'O':
            matrix[i][j] = True

ans = INF

for step in range(1 << N):
    cnt = 0
    tmp_matrix = [row[:] for row in matrix]
    for bit in range(N):
        if step & (1 << bit):
            cnt += 1
            toggle(0, bit)

    for x in range(1, N):
        for y in range(N):
            if tmp_matrix[x-1][y]:
                toggle(x, y)
                cnt += 1

    if not islight():
        ans = min(cnt, ans)
if ans == INF:
    print(-1)
else:
    print(ans)