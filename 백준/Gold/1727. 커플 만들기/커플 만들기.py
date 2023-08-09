N, M = map(int, input().split())
males = sorted([0] + list(map(int, input().split())))
females = sorted([0] + list(map(int, input().split())))
dp = [[0] * (M + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, M + 1):
        prev = dp[i - 1][j - 1]
        temp = abs(males[i] - females[j])
        if i == j:
            dp[i][j] = prev + temp
        elif i > j:
            dp[i][j] = min(prev + temp, dp[i - 1][j])
        else:
            dp[i][j] = min(prev + temp, dp[i][j - 1])

print(dp[N][M])