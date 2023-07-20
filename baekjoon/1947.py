N = int(input())
MOD = 1000000000

dp = [0] * max(3, N + 1)
dp[2] = 1

for i in range(3, N + 1):
    dp[i] = ((i - 1) * (dp[i - 1] + dp[i - 2])) % MOD

print(dp[N])