MOD = 10**9 + 9
n = int(input())
if n == 1:
    print(0)
else:
    dp = [0, 1, 1]
    for _ in range(n - 1):
        new_dp = [0] * 3
        for r in range(3):
            for d in (0, 1, 2):
                new_r = (r + d) % 3
                new_dp[new_r] = (new_dp[new_r] + dp[r]) % MOD
        dp = new_dp
    print(dp[0] % MOD)