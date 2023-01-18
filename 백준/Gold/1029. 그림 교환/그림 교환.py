import sys
input = sys.stdin.readline
N = int(input())
matrix = [list(map(int, input().strip())) for _ in range(N)]
dp = [[[-1] * (1 << N) for _ in range(N)] for _ in range(10)]
def dfs(price, node, bit):
    if dp[price][node][bit] != -1:
        return dp[price][node][bit]
    dp[price][node][bit] = 0
    for next_node in range(1, N):
        if matrix[node][next_node] >= price and not (bit & 1 << next_node):
            dp[price][node][bit] = max(dp[price][node][bit], dfs(matrix[node][next_node], next_node, bit | 1 << next_node) + 1)
    return dp[price][node][bit]

print(dfs(0, 0, 1) + 1)