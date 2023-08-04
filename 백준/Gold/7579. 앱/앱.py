N, M = map(int, input().split())

memory = [0] + list(map(int, input().split()))
cost = [0] + list(map(int, input().split()))
dp = [0] * 10001

for i in range(1, N + 1):
    for j in range(10000, 0, -1):
        if j >= cost[i]:
            dp[j] = max(dp[j], dp[j - cost[i]] + memory[i])

cost = 0
while dp[cost] < M:
    cost += 1

print(cost)