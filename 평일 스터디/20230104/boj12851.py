from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().rstrip().split())
dp = [-1] * 100001
start = deque()
start.append(N)
dp[N] = 0
cnt = 0
while start:
    x = start.popleft()
    if x == K:
        cnt += 1
    for i in (x-1, x+1, x*2):
        if 0 <= i < 100001:
            if dp[i] == -1 or dp[i] == dp[x] + 1:
                dp[i] = dp[x] + 1
                start.append(i)
print(dp[K])
print(cnt)