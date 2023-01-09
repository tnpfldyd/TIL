MOD = 1000000
pisano = 15 * MOD // 10
dp = [0] * (pisano)
dp[1] = 1
for i in range(2, pisano):
    dp[i] = (dp[i-1] + dp[i-2]) % MOD
N = int(input())
print(dp[N%pisano])