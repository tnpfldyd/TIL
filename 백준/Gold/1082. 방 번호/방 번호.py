N = int(input())
P = list(map(int, input().split()))
M = int(input())
dp = [-1] * (M + 1)
for i in range(N - 1, -1, -1):
    for j in range(P[i], M + 1):
        dp[j] = max(dp[j], i, dp[j - P[i]] * 10 + i)

print(dp[M])