N = int(input())
person = [0] + list(map(int, input().split()))
prefix_sum = [0] * (N + 1)

for i in range(1, N + 1):
    prefix_sum[i] = prefix_sum[i - 1] + person[i]
M = int(input())
dp = [[0] * (N + 1) for _ in range(4)]
for i in range(1, 4):
    for j in range(i * M, N + 1):
        dp[i][j] = max(dp[i][j - 1], dp[i - 1][j - M] + (prefix_sum[j] - prefix_sum[j - M]))

print(dp[3][N])