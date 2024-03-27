import sys
input = sys.stdin.readline
T, W = map(int, input().split())
dp = [[[0] * (W + 2) for _ in range(T + 1)] for _ in range(3)]
arr = [0] + [int(input()) for _ in range(T)]
ans = 0

for i in range(1, T + 1):
    for j in range(1, W + 2):
        if arr[i] == 1:
            dp[1][i][j] = max(dp[1][i - 1][j], dp[2][i - 1][j - 1]) + 1
            dp[2][i][j] = max(dp[1][i - 1][j - 1], dp[2][i - 1][j])
        else:
            if i == 1 and j == 1:
                continue
            dp[1][i][j] = max(dp[2][i - 1][j - 1], dp[1][i - 1][j])
            dp[2][i][j] = max(dp[1][i - 1][j - 1], dp[2][i - 1][j]) + 1

for i in range(1, W + 2):
    ans = max(ans, max(dp[1][T][i], dp[2][T][i]))

print(ans)