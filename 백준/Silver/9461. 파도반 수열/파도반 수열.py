import sys
input = sys.stdin.readline
dp = [0] * 101
dp[1] = 1; dp[2] = 1
for i in range(3, 101):
    dp[i] = dp[i-2] + dp[i-3]
T = int(input())
for i in range(T):
    N = int(input())
    print(dp[N])