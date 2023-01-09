N = int(input())
dp = [0] * (N+1)
dp[1] = 1
for i in range(2, N+1):
    dp[i] = dp[i-1] + 1
    if not i % 2:
        dp[i] = min(dp[i], dp[i//2] + 1)
    if not i % 3:
        dp[i] = min(dp[i], dp[i//3] + 1)
print(dp[N]-1)
while N:
    print(N, end= ' ')
    if dp[N] == dp[N-1] + 1:
        N -= 1
    elif not N % 2 and dp[N] == dp[N//2] + 1:
        N //= 2
    elif not N % 3 and dp[N] == dp[N//3] + 1:
        N //= 3
