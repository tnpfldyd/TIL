import sys
import bisect

input = sys.stdin.readline

n = int(input())

meetings = []
for _ in range(n):
    start, end, people = map(int, input().split())
    meetings.append((start, end, people))

meetings.sort(key=lambda x: x[1])

end_times = [meeting[1] for meeting in meetings]

dp = [0] * n
dp[0] = meetings[0][2]

for i in range(1, n):
    current_start = meetings[i][0]
    j = bisect.bisect_right(end_times, current_start) - 1

    if j >= 0:
        current_max = dp[j] + meetings[i][2]
    else:
        current_max = meetings[i][2]

    dp[i] = max(dp[i - 1], current_max)

print(dp[-1])