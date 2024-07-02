n = int(input())
num = list(map(int, input().split()))

dp = [[0] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if num[-i] == num[j - 1]: 
            dp[i][j] = dp[i - 1][j - 1]+1
        else: 
            dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
print(n - dp[n][n])