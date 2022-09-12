import sys
def dfs(x, y, cmd):
    global cnt
    if x == N-1 and y == N-1:
        cnt += 1
        return
    if cmd == 0 or cmd == 1 or cmd == 2:
        nx, ny = x + 1, y + 1
        if 0 <= nx < N and 0 <= ny < N:
            if matrix[nx][ny] != 1 and matrix[x + 1][y] != 1 and matrix[x][y + 1] != 1:
                dfs(nx, ny, 1)
    if cmd == 0 or cmd == 1:
        nx, ny = x, y + 1
        if 0 <= nx < N and 0 <= ny < N:
            if matrix[nx][ny] != 1:
                dfs(nx, ny, 0)
    if cmd == 1 or cmd == 2:
        nx, ny = x + 1, y
        if 0 <= nx < N and 0 <= ny < N:
            if matrix[nx][ny] != 1:
                dfs(nx, ny, 2)
input = sys.stdin.readline
N = int(input())
matrix = [list(map(int, input().rstrip().split())) for _ in range(N)]
cnt = 0
if matrix[N-1][N-1] == 1:
    print(0)
else:
    dfs(0, 1, 0)
    print(cnt)