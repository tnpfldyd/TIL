n, s, m = map(int, input().split())
v = list(map(int, input().split()))

dp = [[0] * (m+1) for i in range(n+1)]

dp[0][s] = 1

for i in range(1, n+1):
    for j in range(m+1):
        if dp[i-1][j] != 0:
            if 0 <= j + v[i-1] <= m:
                dp[i][j + v[i-1]] = 1
            if 0 <= j - v[i-1] <= m:
                dp[i][j - v[i-1]] = 1

ans = -1 
dp = dp[n]
for i in range(m, -1, -1):
    if dp[i] == 1:
        ans = i 
        break 
print(ans)