import sys
input = sys.stdin.readline

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

dp = [[[float('inf')] * 3 for _ in range(M)] for _ in range(N + 1)]
dp[0] = [[0, 0, 0] for _ in range(M)]

for i in range(1, N + 1):
    for j in range(M):
        if j < M - 1:
            dp[i][j][0] = min(dp[i - 1][j + 1][1], dp[i - 1][j + 1][2]) + matrix[i - 1][j]
        if j > 0:
            dp[i][j][2] = min(dp[i - 1][j - 1][1], dp[i - 1][j - 1][0]) + matrix[i - 1][j]
        dp[i][j][1] = min(dp[i - 1][j][0], dp[i - 1][j][2]) + matrix[i - 1][j]

result = min(min(dp[N][j]) for j in range(M))
print(result)