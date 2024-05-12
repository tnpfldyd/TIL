from math import gcd
import sys
input = sys.stdin.readline

mod = 10000003

N = int(input())

nums = [int(input()) for _ in range(N)]
dp = [[0] * 100001 for _ in range(N)]

for i in range(N):
    dp[i][nums[i]] = 1

for i in range(1, N):
    for j in range(1, 100001):
        dp[i][j] += dp[i - 1][j]
        dp[i][j] %= mod
        
        cop = gcd(nums[i], j)
        dp[i][cop] += dp[i - 1][j]
        dp[i][cop] %= mod

print(dp[N - 1][1])
