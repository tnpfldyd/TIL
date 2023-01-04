import sys
input = sys.stdin.readline

alpha, bravo = ' ' + input().strip(), ' ' + input().strip()
N, M = len(alpha), len(bravo)
dp = [[0] * M for _ in range(N)]

for i in range(1, N):
    for j in range(1, M):
        if alpha[i] == bravo[j]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
print(dp[N-1][M-1])
