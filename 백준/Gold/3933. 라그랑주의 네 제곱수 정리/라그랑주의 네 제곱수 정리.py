dp = [[0] * 32768 for _ in range(5)]

dp[0][0] = 1
for i in range(1, 182):
    for k in range(1, 5):
        for ii in range(i * i, 32768):
            dp[k][ii] += dp[k - 1][ii - i * i]

while True:
    N = int(input())
    if N == 0:
        break
    print(dp[1][N] + dp[2][N] + dp[3][N] + dp[4][N])