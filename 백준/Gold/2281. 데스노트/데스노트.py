import sys
input = sys.stdin.readline
INF = sys.maxsize
N_MAX = 1000
N, M = map(int, input().split())
names = [int(input()) for _ in range(N)]

dp = [INF] * N_MAX

def solve(idx):
    if dp[idx] < INF:
        return dp[idx]

    remain = M - names[idx]

    for i in range(idx + 1, N + 1):
        if remain < 0:
            break
        if i == N:
            dp[idx] = 0
            break
        dp[idx] = min(dp[idx], remain * remain + solve(i))
        remain -= names[i] + 1

    return dp[idx]

dp[N - 1] = 0

print(solve(0))
