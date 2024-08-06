W, H = map(int, input().split())
MOD = 100000
dp = [[[[0] * 2 for _ in range(2)] for _ in range(101)] for _ in range(101)]
for i in range(2, W + 1):
    dp[i][1][0][0] = 1
for i in range(2, H + 1):
    dp[1][i][1][0] = 1
for i in range(2, W + 1):
    for j in range(2, H + 1):
        dp[i][j][0][0] = (dp[i - 1][j][0][0] + dp[i - 1][j][0][1]) % MOD
        dp[i][j][0][1] = dp[i - 1][j][1][0]
        dp[i][j][1][0] = (dp[i][j - 1][1][0] + dp[i][j - 1][1][1]) % MOD
        dp[i][j][1][1] = dp[i][j - 1][0][0]
result = 0
for i in range(2):
    for j in range(2):
        result += dp[W][H][i][j]
print(result % MOD)