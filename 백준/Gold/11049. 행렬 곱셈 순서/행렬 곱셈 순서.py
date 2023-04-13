import sys
input = sys.stdin.readline
INF = sys.maxsize
N = int(input())

matrix = []
for i in range(N):
    a, b = map(int, input().split())
    matrix.append([a, b])

dp = [[0] * N for _ in range(N)]

for i in range(1, N):
    for j in range(N - i):
        dp[j][i + j] = INF
        for k in range(j, i + j):
            dp[j][i + j] = min(dp[j][i + j], dp[j][k] + dp[k + 1][i + j] + matrix[j][0] * matrix[k][1] * matrix[i + j][1])

print(dp[0][N - 1])