MOD = 987654321

n = int(input())
n //= 2
dp = [0] * (n + 1)
dp[0] = 1

for i in range(1, n + 1):
    for j in range(i):
        dp[i] += (dp[j] * dp[i - 1 - j]) % MOD
    dp[i] %= MOD

print(dp[n] % MOD)