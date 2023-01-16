import sys
input = sys.stdin.readline
N, M, C = map(int, input().split())
W = [list(map(int, input().strip().split())) for _ in range(C)]
A = list(map(lambda x : int(x) - 1, input().split()))
B = list(map(lambda x : int(x) - 1, input().split()))
dp = [[0] * M for _ in range(N)]

for i in range(N):
    for j in range(M):
        num1 = W[A[i]][B[j]]
        if i > 0 and j > 0:
            num1 += dp[i-1][j-1]
        num2 = 0
        if i > 0:
            num2 = dp[i-1][j]
        num3 = 0
        if j > 0:
            num3 = dp[i][j-1]
        dp[i][j] = max(num1, num2, num3)

print(dp[N-1][M-1])