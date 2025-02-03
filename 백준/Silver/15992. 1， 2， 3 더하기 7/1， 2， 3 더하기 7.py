import sys
input = sys.stdin.readline

MOD = 10**9 + 9
max_n = 1000

dp = [[0] * (max_n + 1) for _ in range(max_n + 1)]
dp[1][1] = 1
dp[2][1] = 1
dp[3][1] = 1

for i in range(1, max_n + 1):
    for j in range(1, i + 1):
        if i in (1, 2, 3) and j == 1:
            continue
        total = 0
        if i - 1 >= 0 and j - 1 >= 0:
            total += dp[i - 1][j - 1]
        if i - 2 >= 0 and j - 1 >= 0:
            total += dp[i - 2][j - 1]
        if i - 3 >= 0 and j - 1 >= 0:
            total += dp[i - 3][j - 1]
        dp[i][j] = total % MOD

T = int(input())

for _ in range(T):
    n, m = map(int, input().split())
    print(dp[n][m] % MOD)