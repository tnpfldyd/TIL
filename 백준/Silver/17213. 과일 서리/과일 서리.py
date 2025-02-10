n = int(input())
m = int(input())

dp = [[0] * m for _ in range(n)]
for j in range(m):
    dp[0][j] = 1

for i in range(1, n):
    dp[i][i] = 1
    for j in range(i + 1, m):
        dp[i][j] = dp[i - 1][j - 1] + dp[i][j - 1]

print(dp[-1][-1])