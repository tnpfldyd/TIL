import sys
input = sys.stdin.readline
dp = [1] * 1005

for i in range(1, 1001):
    for j in range(i):
        if (i - j) & 1:
            continue
        dp[i] += dp[(i - j) >> 1]

t = int(input())
for _ in range(t):
    n = int(input())
    print(dp[n])