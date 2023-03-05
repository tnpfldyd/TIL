import sys
sys.setrecursionlimit(10 ** 7)
N, M, K = int(input()), int(input()), int(input())

dp = [[[-1] * (K + 1) for _ in range(M + 1)] for _ in range(N + 1)]

def dfs(n, m, k):
    if n < 0 or m < 0 or k < 0:
        return 0
    if not k:
        return 1
    if dp[n][m][k] != -1:
        return dp[n][m][k]
    ret = 0
    ret += dfs(n-1, m, k)
    ret += dfs(n-1, m-1, k-1) * m
    ret += dfs(n-1, m-2, k-2) * m * (m-1) // 2 # m-1 C k-2 = (m-1)! / ((k-2)! * (m-1-(k-2))!) = (m-1) * (m-2) / 2 (n-1) 행까지 모두 채우고, (m-2) 열에 룩을 놓을 때, 이 중에서 서로 공격할 수 없는 (k-2) 개의 룩을 선택하는 경우의 수를 계산하는 것
    ret += dfs(n-2, m-1, k-2) * m * (n-1) # (m-1)C1 * (n-1)C2 = (m-1) * (n-1) * (n-2) // 2 (n-1)개의 행 중에 2개를 선택하고, 각각에 룩을 놓는 경우의 수를 곱한 것
    ret %= 1000001
    dp[n][m][k] = ret
    return ret
print(dfs(N, M, K))