import sys
input = sys.stdin.readline

MOD = 1_000_000_009
MAX_N = 1000

dp = [[0] * (MAX_N + 1) for _ in range(MAX_N + 1)]
dp[0][0] = 1

for k in range(1, MAX_N + 1):
    for s in range(1, MAX_N + 1):
        if s - 1 >= 0:
            dp[k][s] += dp[k - 1][s - 1]
        if s - 2 >= 0:
            dp[k][s] += dp[k - 1][s - 2]
        if s - 3 >= 0:
            dp[k][s] += dp[k - 1][s - 3]
        dp[k][s] %= MOD

T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    ans = 0
    for k in range(1, m + 1):
        ans = (ans + dp[k][n]) % MOD
    print(ans)