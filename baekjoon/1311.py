import sys
input = sys.stdin.readline
INF = sys.maxsize
N = int(input())
matrix = [list(map(int, input().strip().split())) for _ in range(N)]
dp = [[-1] * (1 << N) for _ in range(N)]

def bit(node, visited):
    if visited == (1 << N) - 1:
        return 0
    if dp[node][visited] != -1:
        return dp[node][visited]
    
    dp[node][visited] = INF
    for i in range(N):
        if visited & (1 << i):
            continue
        dp[node][visited] = min(dp[node][visited], bit(node + 1, visited | (1 << i)) + matrix[node][i])
    return dp[node][visited]

print(bit(0, 0))


