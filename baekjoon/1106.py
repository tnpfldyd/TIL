import sys
input = sys.stdin.readline
INF = sys.maxsize

C, N = map(int, input().split())
orders = [tuple(map(int, input().split())) for _ in range(N)]
dp = [INF] * (C + 100)
dp[0] = 0
for cost, people in orders:
    for i in range(people, C + 100):
        if dp[i - people] != INF:
            dp[i] = min(dp[i], dp[i - people] + cost)

answer = INF

for i in range(C, C + 100):
    answer = min(answer, dp[i])

print(answer)