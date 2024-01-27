N = int(input())
weight = list(map(int, input().split()))
total = max(weight)

dp = [[False] * (40001) for _ in range(N + 1)]
dp[0][0] = True

for i in range(N):
    for j in range(40001):
        if dp[i][j]:
            dp[i + 1][j + weight[i - 1]] = True
            dp[i + 1][j] = True
            dp[i + 1][abs(j - weight[i - 1])] = True
M = int(input())
check_list = list(map(int, input().split()))
for check in check_list:
    print('Y' if dp[N][check] else 'N', end=' ')