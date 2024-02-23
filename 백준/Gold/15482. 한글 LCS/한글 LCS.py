s1 = input()
s2 = input()

N = len(s1)
M = len(s2)

dp = [[0] * (M + 1) for _ in range(N + 1)]

for i in range(N):
    for j in range(M):
        if s1[i] == s2[j]:
            dp[i + 1][j + 1] = dp[i][j] + 1
        else:
            dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])

print(dp[N][M])