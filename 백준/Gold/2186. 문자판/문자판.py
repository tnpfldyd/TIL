import sys

input = sys.stdin.readline
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y, idx):
    if idx == len(word):
        return 1
    if c[x][y][idx] != -1:
        return c[x][y][idx]

    c[x][y][idx] = 0
    for i in range(4):
        temp_x, temp_y = x, y
        for _ in range(K):
            nx = temp_x + dx[i]
            ny = temp_y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if a[nx][ny] == word[idx]:
                    c[x][y][idx] += dfs(nx, ny, idx+1)
            temp_x, temp_y = nx, ny
    return c[x][y][idx]

N, M, K = map(int, input().split())
a = []
for _ in range(N):
    a.append(list(input().strip()))
word = list(input().strip())

start = []
for i in range(N):
    for j in range(M):
        if a[i][j] == word[0]:
            start.append([i, j])

ans =  0
c = [[[-1] * len(word) for _ in range(M)] for _ in range(N)]
for i in range(len(start)):
    x, y = start[i]
    ans += dfs(x, y, 1)
print(ans)