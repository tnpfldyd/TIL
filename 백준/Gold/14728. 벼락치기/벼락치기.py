import sys
input = sys.stdin.readline

N, T = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(N)]
dp = [[0] * (T + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    time, point = points[i - 1]
    for j in range(T + 1):
        if j < time:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - time] + point)

print(dp[N][T])