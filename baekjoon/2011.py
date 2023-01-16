import sys
sys.setrecursionlimit(10**6)
N = input()
dp = [-1] * len(N)

def dfs(n):
    if n == len(N):
        return 1
    if dp[n] != -1:
        return dp[n]
    dp[n] = 0
    if N[n] != '0':
        dp[n] += dfs(n + 1)
        if n + 1 < len(N) and int(N[n:n+2]) <= 26:
            dp[n] += dfs(n + 2)
    return dp[n] % 1000000
print(dfs(0))