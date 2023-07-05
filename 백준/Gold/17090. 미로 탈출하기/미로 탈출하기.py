import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
N, M = map(int, input().split())
MAP = [list(input().strip()) for _ in range(N)]
dp = [[-1] * M for _ in range(N)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
answer = 0

def dir_to_idx(x):
    if x == 'U':
        return 3
    elif x == 'R':
        return 0
    elif x == 'D':
        return 2
    elif x == 'L':
        return 1

def dfs(x, y):
    if x < 0 or y < 0 or x >= N or y >= M:
        return 1
    if dp[x][y] != -1:
        return dp[x][y]

    dp[x][y] = 0
    dir = dir_to_idx(MAP[x][y])
    dp[x][y] = dfs(x + dx[dir], y + dy[dir])

    return dp[x][y]

for i in range(N):
    for j in range(M):
        answer += dfs(i, j)
print(answer)
