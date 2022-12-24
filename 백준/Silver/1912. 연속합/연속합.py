import sys
INF = sys.maxsize
N = int(input())
dp = [0] * (N+1)
N_list = list(map(int, input().strip().split()))
result = -INF
for idx, cost in enumerate(N_list, 1):
    dp[idx] = max(dp[idx-1] + cost, cost)
    result = max(result, dp[idx])
print(result)