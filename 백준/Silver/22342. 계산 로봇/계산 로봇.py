import sys
input = sys.stdin.readline
NMAX = 2010

M, N = map(int, input().split())
grid = [[0] * (N + 1)] + [[0] + list(map(int, input().strip())) for _ in range(M)]
dp = [[0] * (N + 1) for _ in range(NMAX)]
max_values = [[0] * (N + 1) for _ in range(NMAX)]

max_result = 0

for col in range(1, N + 1):
    for row in range(1, M + 1):
        for offset in range(-1, 2):
            dp[row][col] = max(dp[row][col], max_values[row + offset][col - 1])
        max_values[row][col] = dp[row][col] + grid[row][col]
        max_result = max(max_result, dp[row][col])

print(max_result)