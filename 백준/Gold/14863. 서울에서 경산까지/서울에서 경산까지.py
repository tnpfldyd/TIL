import sys
input = sys.stdin.readline
INF = sys.maxsize

N, K = map(int, input().split())
time_cost_array = [tuple(map(int, input().split())) for _ in range(N)]
dp = [[-1] * (K + 1) for _ in range(N + 1)]

def solve(n, k):
    if k > K: return -INF
    if n == N: return 0
    ret = dp[n][k]
    if ret != -1: return ret
    ft, fp, bt, bp = time_cost_array[n]
    ret = max(solve(n + 1, k + ft) + fp, solve(n + 1, k + bt) + bp)
    dp[n][k] = ret
    return ret

result = solve(0, 0)
print(result)