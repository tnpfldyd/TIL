import sys
input = sys.stdin.readline

dp = [[0] * 31 for _ in range(31)]
for i in range(31):
    for j in range(i, 31):
        if not i:
            dp[i][j] = 1
        else:
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

while True:
    N = int(input())
    if not N:
        break
    print(dp[N][N])