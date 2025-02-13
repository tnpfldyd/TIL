MOD = 1_000_000_007

def count_combinations(N, M):
    dp = [0] * (N + 1)
    dp[0] = 1

    for i in range(1, N + 1):
        dp[i] = dp[i - 1]
        if i >= M:
            dp[i] = (dp[i] + dp[i - M]) % MOD

    return dp[N]

N, M = map(int, input().split())
print(count_combinations(N, M))