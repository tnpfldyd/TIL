import sys
input = sys.stdin.readline
INF = sys.maxsize
D, P = map(int, input().split())

arr = [tuple(map(int, input().split())) for _ in range(P)]

dp = [0] * (D + 1)
dp[0] = INF

for i in range(P):
    for j in range(D, arr[i][0] - 1, -1):
        dp[j] = max(dp[j], min(dp[j - arr[i][0]], arr[i][1]))

print(dp[D])
