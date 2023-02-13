N = int(input())
mod = 9901
dp = [[1] * (N + 1) for _ in range(3)]
for i in range(2, N+1):
    dp[0][i] = (dp[1][i-1] + dp[2][i-1]) % mod
    dp[1][i] = (dp[0][i-1] + dp[2][i-1]) % mod
    dp[2][i] = (dp[0][i-1] + dp[1][i-1] + dp[2][i-1]) % mod
print((dp[0][N] + dp[1][N] + dp[2][N]) % mod)