import sys
input = sys.stdin.readline
N, T = map(int, input().split())
d, m = [0], [0]
day = cost = 0
for _ in range(N):
    a, b = map(int, input().split())
    day += a
    cost += b
    d.append(a); m.append(b)
    
dp = [[0] * (T + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    for j in range(1, T + 1):
        if j - d[i] < 0:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - d[i]] + m[i])
            
print(cost - dp[N][T])