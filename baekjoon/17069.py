import sys
input = sys.stdin.readline

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]

dp = [[[0] * N for _ in range(N)] for _ in range(3)]

dp[0][0][1] = 1

for i in range(1, N - 1):
    if matrix[0][i + 1]: break

    dp[0][0][i + 1] = dp[0][0][i]

for i in range(1, N):
    for j in range(1, N):
        if matrix[i][j]: continue

        dp[0][i][j] = dp[0][i][j - 1] + dp[1][i][j - 1]
        dp[2][i][j] = dp[1][i - 1][j] + dp[2][i - 1][j]

        if matrix[i - 1][j] or matrix[i][j - 1]: continue

        dp[1][i][j] = dp[0][i - 1][j - 1] + dp[1][i - 1][j - 1] + dp[2][i - 1][j - 1]

result = 0
for i in range(3):
    result += dp[i][N - 1][N - 1]

print(result)