N = int(input())

dp = [0] * (N + 1)
dp[0] = dp[1] = 1

for i in range(2, N + 1):
    dp[i] += dp[i - 1] + dp[i - 2] * 2
    
temp = dp[N] + dp[N // 2]
print(temp // 2 if N % 2 else (temp + dp[N // 2 - 1] * 2) // 2)