import sys
input = sys.stdin.readline

N, M, H = map(int, input().split())
dp = [[1] + [0] * H]

for i in range(1, N + 1):
    arr = dp[i - 1].copy()
    blocks = list(map(int, input().split()))

    for high in blocks:
        for j in range(high, H + 1):
            arr[j] += dp[i - 1][j - high]
            arr[j] %= 10007

    dp.append(arr)
print(dp[N][H])