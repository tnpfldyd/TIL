import sys
input = sys.stdin.readline
N = int(input())
matrix = []
for _ in range(N):
    arr = list(map(int, input().strip().split()))
    matrix.append(arr)
dp = [-1] * (1 << N)

def dfs(node, bit):
    if bit == (1 << N) - 1:
        return 1
    if dp[bit] != -1:
        return dp[bit]
    dp[bit] = 0
    for i in range(N):
        if bit & 1 << i:
            continue
        dp[bit] = max(dp[bit], dfs(node + 1, bit | 1 << i) * matrix[node][i])
    return dp[bit]

print("{:.6f}".format(dfs(0, 0)/(100 ** (N-1))))