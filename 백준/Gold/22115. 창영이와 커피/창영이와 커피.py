MAX_K = 100001
INF = 1e9

N, K = map(int, input().split())
C = [0] + list(map(int, input().split()))

dp = [INF] * MAX_K
dp[0] = 0

for i in range(1, N + 1):
    for j in range(K, C[i] - 1, -1):
        if j - C[i] >= 0:
            dp[j] = min(dp[j], dp[j - C[i]] + 1)

print(dp[K] if dp[K] != INF else -1)