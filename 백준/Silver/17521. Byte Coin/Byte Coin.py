import sys
input = sys.stdin.readline
n, W = map(int, input().split())
p = [0] + [int(input()) for _ in range(n)]
dp = [0] * (n + 1)
dp[1] = W

for i in range(2, n + 1):
    b = dp[i - 1]
    si = p[i]
    for j in range(1, i):
        mj = dp[j]
        cur = (mj % p[j]) + (mj // p[j]) * si
        if cur > b:
            b = cur
    dp[i] = b

print(dp[n])