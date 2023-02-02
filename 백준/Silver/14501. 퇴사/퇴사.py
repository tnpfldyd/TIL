import sys
input = sys.stdin.readline
N = int(input())
orders = []
for _ in range(N):
    orders.append(tuple(map(int, input().strip().split())))
dp = [0] * (N + 1)
for i in range(N-1, -1, -1):
    day, money = orders[i]
    deadline = i + day
    if deadline > N:
        dp[i] = dp[i + 1]
    else:
        dp[i] = max(dp[i + 1], dp[deadline] + money)
print(dp[0])