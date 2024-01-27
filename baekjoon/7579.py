import sys
input = sys.stdin.readline
INF = sys.maxsize
N, M = map(int, input().split())

memory = [0] + list(map(int, input().split()))
cost = [0] + list(map(int, input().split()))
temp = sum(cost)
dp = [[0] * (temp + 1) for _ in range(N + 1)]

answer = INF

for i in range(1, N + 1):
    cur_cost = cost[i]
    cur_memory = memory[i]
    for j in range(temp + 1):
        if j >= cost[i]:
            dp[i][j] = max(dp[i-1][j - cur_cost] + cur_memory, dp[i-1][j])
        else:
            dp[i][j] = dp[i - 1][j]
        if dp[i][j] >= M:
            answer = min(answer, j)

print(answer)