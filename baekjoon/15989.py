import sys
input = sys.stdin.readline

N = int(input())

dp = [[0] * 10001 for _ in range(4)]

for i in range(1, 4):
    for j in range(1, i + 1):
        dp[j][i] = 1

for i in range(4, 10001):
    dp[1][i] = dp[1][i - 1]
    dp[2][i] = dp[1][i - 2] + dp[2][i - 2]
    dp[3][i] = dp[1][i - 3] + dp[2][i - 3] + dp[3][i - 3]

for _ in range(N):
    number = int(input())
    result = 0
    for i in range(1, 4):
        result += dp[i][number]
    print(result)