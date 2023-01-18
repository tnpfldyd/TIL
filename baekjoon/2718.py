import sys
input = sys.stdin.readline
T = int(input())
dp = [0] * 30
dp[0], dp[1], dp[2], dp[3] = 1, 5, 11, 36
temp = 4
for _ in range(T):
    n = int(input())
    if not dp[n-1]:
        for i in range(temp, n):
            dp[i] = dp[i-1] + dp[i-2]*5 + dp[i-3] - dp[i-4]
    print(dp[n-1])
    temp = max(temp, n)
