N = int(input())
a = list(map(int, input().split()))

dp = [[0] * 21 for _ in range(N)]

dp[0][a[0]] = 1

for i in range(1, N - 1):
    for j in range(21):
        for k in range(2):
            if k:
                next_num = j - a[i]
            else:
                next_num = j + a[i]
            
            if 0 <= next_num <= 20:
                dp[i][next_num] += dp[i - 1][j]

print(dp[N - 2][a[N - 1]])