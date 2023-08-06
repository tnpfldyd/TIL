import sys
input = sys.stdin.readline
INF = sys.maxsize
N, K = map(int, input().split())
money = [0] + [int(input()) for _ in range(N)]
dp = [INF] * (K + 1)
dp[0] = 0
for i in range(1, N + 1):
    for j in range(money[i] , K + 1):
        dp[j] = min(dp[j], dp[j - money[i]] + 1)

print(dp[K] if dp[K] != INF else -1)