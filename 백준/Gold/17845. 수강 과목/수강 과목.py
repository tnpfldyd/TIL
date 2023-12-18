import sys
input = sys.stdin.readline

N, K = map(int, input().split())
times = [(0, 0)] + [tuple(map(int, input().split())) for _ in range(K)]
dp = [[0] * (N + 1) for _ in range(K + 1)]

result = 0

for i in range(1, K + 1):
    cur_i, cur_t = times[i]
    for j in range(1, N + 1):
        dp[i][j] = dp[i - 1][j] if cur_t > j else max(dp[i - 1][j], dp[i - 1][j - cur_t] + cur_i)
        result = max(result, dp[i][j])

print(result)