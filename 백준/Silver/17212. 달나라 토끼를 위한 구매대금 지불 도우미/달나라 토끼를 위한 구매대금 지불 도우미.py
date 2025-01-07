import sys
input = sys.stdin.readline

n = int(input())

dp = [float('inf')] * (n + 1)
dp[0] = 0

steps = [1, 2, 5, 7]

for i in range(1, n + 1):
    for step in steps:
        if i >= step:
            dp[i] = min(dp[i], dp[i - step] + 1)
        else:
            break

print(dp[n])