N = int(input())
dp = [0] * (N + 1)
for i in range(1, N + 1):
    dp[i] = dp[i - 1] + 1
    for j in range(3, i):
        dp[i] = max(dp[i], dp[i - j] * (j - 1))
print(dp[N])