import sys
input = sys.stdin.readline
dp = [1, 1, 2, 4]

for _ in range(int(input())):
    n = int(input())
    for i in range(len(dp) - 1, n):
        dp.append(dp[i] + dp[i - 1] + dp[i - 2] + dp[i - 3])
    print(dp[n])