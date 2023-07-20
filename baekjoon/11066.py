import sys
input = sys.stdin.readline
INF = sys.maxsize

T = int(input())

for _ in range(T):
    K = int(input())
    file = list(map(int, input().split()))
    sums = [0] * (K + 1)
    dp = [[0] * (K + 1) for _ in range(K + 1)]

    for i in range(1, K + 1):
        sums[i] = sums[i - 1] + file[i - 1]

    for i in range(1, K + 1):
        for j in range(1, K - i + 1):
            dp[j][i + j] = INF
            for k in range(j, i + j):
                dp[j][i + j] = min(dp[j][i + j], dp[j][k] + dp[k + 1][i + j] + sums[i + j] - sums[j - 1])

    print(dp[1][K])