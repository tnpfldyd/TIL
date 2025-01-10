import sys
input = sys.stdin.readline

n = int(input())
stones = []

dp = [float('inf')] * n
dp[0] = 0

for i in range(n - 1):
    small_jump, big_jump = map(int, input().split())
    stones.append((small_jump, big_jump))
    if i + 1 < n:
        dp[i + 1] = min(dp[i + 1], dp[i] + small_jump)
    if i + 2 < n:
        dp[i + 2] = min(dp[i + 2], dp[i] + big_jump)

k = int(input())
min_cost = dp[-1]

for i in range(3, n):
    jump_cost = dp[i - 3] + k
    next_cost1, next_cost2 = float('inf'), float('inf')
    for j in range(i, n - 1):
        if i + 1 <= n:
            next_cost1 = min(next_cost1, jump_cost + stones[j][0])
        if i + 2 <= n:
            next_cost2 = min(next_cost2, jump_cost + stones[j][1])
        jump_cost, next_cost1, next_cost2 = next_cost1, next_cost2, float('inf')
    min_cost = min(min_cost, jump_cost)

print(min_cost)