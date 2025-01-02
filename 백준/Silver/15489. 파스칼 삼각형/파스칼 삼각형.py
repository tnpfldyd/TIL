import sys
input = sys.stdin.readline

r, c, w = map(int, input().split())
n = r + w - 1
dp = [[0] * n for _ in range(n)]

dp[0][0] = 1
for i in range(1, n):
    dp[i][0] = dp[i - 1][0]
    dp[i][i] = dp[i - 1][i - 1]

for i in range(2, n):
    for j in range(1, i):
        dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]

result = 0
for i in range(w):
    for j in range(i + 1):
        result += dp[r + i - 1][c + j - 1]

print(result)