import sys
input = sys.stdin.readline  

N, M = map(int, input().split())  
dist = [0] + [int(input()) for _ in range(N)]  
dp = [[0] * (M + 1) for _ in range(N + 1)]  

for i in range(1, N + 1):  
    for j in range(1, M + 1):  
        dp[i][j] = dp[i - 1][j - 1] + dist[i]  

    for j in range(1, M + 1):  
        if i - j < 0:  
            break  
        dp[i][0] = max(dp[i][0], dp[i - j][j], dp[i - j][0])  

print(dp[N][0])