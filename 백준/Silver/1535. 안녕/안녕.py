import sys
input = sys.stdin.readline

MAX_HEALTH = 100
TARGET_HEALTH = 99

n = int(input())
health_cost = [0] + list(map(int, input().split()))
happiness = [0] + list(map(int, input().split()))

dp = [[0] * MAX_HEALTH for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, MAX_HEALTH):
        if health_cost[i] <= j:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - health_cost[i]] + happiness[i])
        else:
            dp[i][j] = dp[i - 1][j]

print(dp[n][TARGET_HEALTH])