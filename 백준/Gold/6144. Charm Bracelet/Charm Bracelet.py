import sys
input = sys.stdin.readline

N, M = map(int, input().split())
weights = []
values = []
for _ in range(N):
    w, v = map(int, input().split())
    weights.append(w)
    values.append(v)
    
dp = [0] * (M + 1)
for i in range(N):
    for j in range(M, weights[i] - 1, -1):
        dp[j] = max(dp[j], dp[j - weights[i]] + values[i])

print(dp[M])