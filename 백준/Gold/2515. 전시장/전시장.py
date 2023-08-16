import sys, bisect
input = sys.stdin.readline

N, S = map(int, input().split())
draws = [(0, 0)] + [tuple(map(int, input().split())) for _ in range(N)]
draws.sort()

dp = [[0, 0] for _ in range(N + 1)]
dp[1][0] = draws[1][1]

for i in range(2, N + 1):
    idx = bisect.bisect_right(draws, draws[i][0] - S, key=lambda x : x[0])
    if idx == i + 1:
        dp[i][0] = draws[i][1]
    else:
        dp[i][0] = max(dp[idx - 1][0], dp[idx - 1][1]) + draws[i][1]
    dp[i][1] = max(dp[i - 1][0], dp[i - 1][1])
print(max(dp[N]))