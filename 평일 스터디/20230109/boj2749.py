MOD = 1000000
pisano = 15 * MOD // 10 
# 피사노의 주기 나눌수가 10^k (k > 2)일 때  
# 주기는 15 * 10^(k - 1) 즉 15 * 나눌수 // 10 
dp = [0] * (pisano)
dp[1] = 1
for i in range(2, pisano):
    dp[i] = (dp[i-1] + dp[i-2]) % MOD
N = int(input())
print(dp[N%pisano])