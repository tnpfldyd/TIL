n = int(input())

meetings = []
for _ in range(n):
  meetings.append(list(map(int, input().split())))

meetings.sort()

dp = [0] * n
dp[0] = meetings[0][2]
for i in range(1, n):
  dp[i] = max(dp[i - 1], dp[i - 2] + meetings[i][2])

print(dp[n - 1])