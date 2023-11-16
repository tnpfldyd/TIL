N = int(input())
MOD = 1000000007

dp = [[0]*1516 for _ in range(3)]
dp[0][1] = dp[2][2] = 0
dp[0][2] = dp[1][2] = 1

for i in range(3, N + 1):
    dp[0][i] = (dp[2][i - 1] + dp[1][i - 1]) % MOD
    dp[1][i] = (dp[0][i - 1] + dp[2][i - 1]) % MOD
    dp[2][i] = (dp[1][i - 1] + dp[0][i - 1]) % MOD

print(dp[0][N])