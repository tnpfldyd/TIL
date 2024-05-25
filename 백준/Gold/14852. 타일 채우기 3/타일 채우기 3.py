MOD = 1000000007
N = int(input())
dp = [[0] * 2 for _ in range(N + 3)]
dp[0][0] = 0
dp[1][0] = 2
dp[2][0] = 7
dp[2][1] = 1

for i in range(3, N + 1):
    dp[i][1] = (dp[i - 3][0] + dp[i - 1][1]) % MOD
    dp[i][0] = (3 * dp[i - 2][0] + 2 * dp[i - 1][0] + 2 * dp[i][1]) % MOD

print(dp[N][0])