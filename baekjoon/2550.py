from bisect import bisect_left
import sys
input = sys.stdin.readline

N = int(input())
switchLeft = list(map(int, input().split()))
switchRight = list(map(int, input().split()))
lines = [0] * (N + 1)
for i, num in enumerate(switchRight):
    lines[num] = i + 1

result = []
dp = []

for switch in switchLeft:
    cur = lines[switch]
    if not result or result[-1] < cur:
        dp.append(len(result))
        result.append(cur)
    else:
        idx = bisect_left(result, cur)
        result[idx] = cur
        dp.append(idx)

answer = []
cnt = len(result) - 1
print(cnt + 1)

for i in range(N - 1, -1, -1):
    if dp[i] == cnt:
        answer.append(switchLeft[i])
        cnt -= 1
answer.sort()
print(*answer)