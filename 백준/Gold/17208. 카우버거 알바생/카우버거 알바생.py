import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())

dp = [[[0] * (K + 1) for _ in range(M + 1)] for _ in range(N + 1)]
x = [0] * (N + 1)
y = [0] * (N + 1)

for i in range(1, N + 1):
    x[i], y[i] = map(int, input().split())

for i in range(1, N + 1):
    for j in range(1, M + 1):
        for u in range(1, K + 1):
            if j >= x[i] and u >= y[i]:
                dp[i][j][u] = max(dp[i - 1][j][u], dp[i - 1][j - x[i]][u - y[i]] + 1)
            else:
                dp[i][j][u] = dp[i - 1][j][u]

print(dp[N][M][K])