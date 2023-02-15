import sys
input = sys.stdin.readline
INF = sys.maxsize
N, target = map(int, input().split())
shortcuts = {}
for _ in range(N):
    s, e, cost = map(int, input().split())
    if e not in shortcuts:
        shortcuts[e] = [(s, cost)]
    else:
        shortcuts[e].append((s, cost))

dp = [INF] * (target + 1)

dp[0] = 0
for i in range(1, target + 1):
    if i in shortcuts:
        for shortcut in shortcuts[i]:
            dp[i] = min(dp[i], min(dp[i-1] + 1, shortcut[1] + dp[shortcut[0]]))
    else:
        dp[i] = dp[i-1] + 1
print(dp[target])