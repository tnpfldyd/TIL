import sys
input = sys.stdin.readline
N, M, C = map(int, input().split())
matrix = [list(map(int, input().strip().split())) for _ in range(C)]
N_list = list(map(int, input().strip().split()))
M_list = list(map(int, input().strip().split()))
dp = [[-1] * (M+1) for _ in range(N+1)]

def top(n, m):
    if n == N or m == M:
        return 0
    dp[n][m] = matrix[N_list[n]-1][M_list[m]-1]
    dp[n][m] = max(dp[n][m], top(n+1, m), top(n, m+1), top(n+1, m+1))
    return dp[n][m]
print(top(0,0))
