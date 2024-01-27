N = int(input())
dp = [0] * (N + 1)
MOD = 987654321

dp[0] = 1
dp[2] = 1

for i in range(4, N + 1, 2):
    for j in range(0, i - 1, 2):
        dp[i] += dp[j] * dp[i - j - 2]
        dp[i] %= MOD

print(dp[N])