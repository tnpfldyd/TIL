import sys
input = sys.stdin.readline

N, M = map(int, input().split())

dp = [[0] * (M + 1)] + [[0] + list(map(int, list(input().strip()))) for _ in range(N)]

result = 0

for i in range(1, N + 1):
    for j in range(1, M + 1):
        if dp[i][j]:
            dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
            result = max(result, dp[i][j])

print(result ** 2)