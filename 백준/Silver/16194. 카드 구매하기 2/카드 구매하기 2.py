import sys
input = sys.stdin.readline

n = int(input())
P = [0] + list(map(int, input().split()))
dp = [0 for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, i + 1):
        if dp[i] == 0:
            dp[i] = dp[i - j] + P[j]
        else:
            dp[i] = min(dp[i], dp[i - j] + P[j])

print(dp[n])