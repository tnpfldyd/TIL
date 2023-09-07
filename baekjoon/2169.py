import sys
input = sys.stdin.readline

N, M = map(int,input().split())
dp = [list(map(int,input().split())) for _ in range(N)]

for i in range(1, M):
    dp[0][i] += dp[0][i - 1]

for i in range(1, N):
    left = dp[i][:]
    right = dp[i][:]

    for j in range(M):
        if j == 0:
            left[j] += dp[i - 1][j]
        else:
            left[j] += max(dp[i - 1][j],left[j - 1])

    for j in range(M - 1, -1, -1):
        if j == M - 1:
            right[j] += dp[i - 1][j]
        else:
            right[j] += max(dp[i - 1][j],right[j + 1])

    for j in range(M):
        dp[i][j] = max(left[j], right[j])

print(dp[N-1][M-1])