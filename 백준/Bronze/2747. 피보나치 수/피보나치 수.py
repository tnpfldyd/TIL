dp = [0] * 46
dp[1] = 1
for i in range(2, 46):
    dp[i] = dp[i-1] + dp[i-2]
N = int(input())
print(dp[N])