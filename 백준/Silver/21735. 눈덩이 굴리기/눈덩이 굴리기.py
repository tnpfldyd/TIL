N, M = map(int, input().split())
a = [0] + list(map(int, input().split()))

dp = [[-1] * (N + 1) for _ in range(M + 1)]
dp[0][0] = 1

for t in range(M):
    for i in range(N + 1):
        if dp[t][i] == -1:
            continue

        cur = dp[t][i]

        if i == N:
            continue

        if i + 1 <= N:
            dp[t + 1][i + 1] = max(dp[t + 1][i + 1], cur + a[i + 1])

        if i + 2 <= N:
            dp[t + 1][i + 2] = max(dp[t + 1][i + 2], cur // 2 + a[i + 2])

ans = 0
for t in range(M + 1):
    for i in range(N + 1):
        ans = max(ans, dp[t][i])

print(ans)