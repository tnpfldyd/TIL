import sys
input = sys.stdin.readline
N = int(input())
dp = [0] * 10000
stairs = [0] * 10000
for i in range(N):
    stairs[i] = int(input())
dp[0] = stairs[0]
dp[1] = stairs[0]+stairs[1]
dp[2] = max(stairs[0]+stairs[2], stairs[1]+stairs[2], dp[1])
for i in range(3, N):
    dp[i] = max(dp[i-2] + stairs[i], dp[i-3] + stairs[i-1] + stairs[i])
    dp[i] = max(dp[i-1], dp[i])
print(dp[N-1])