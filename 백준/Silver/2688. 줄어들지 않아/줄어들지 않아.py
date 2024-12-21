import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    dp = [[0] * 10 for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        dp[i][0] = sum(dp[i - 1]) if i > 1 else 1
        for j in range(1, 10):
            dp[i][j] = max(1, dp[i][j - 1] - dp[i - 1][j - 1])
    
    print(sum(dp[n]))