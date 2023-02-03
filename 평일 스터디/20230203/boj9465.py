import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    sticker = []
    for i in range(2):
        sticker_list = list(map(int, input().strip().split()))
        sticker.append([0] + sticker_list)
    dp = [[0] * (N + 1) for _ in range(2)]
    dp[0][1], dp[1][1] = sticker[0][1], sticker[1][1]
    for i in range(2, N + 1):
        dp[0][i] = max(dp[1][i - 1], dp[1][i - 2]) + sticker[0][i]
        dp[1][i] = max(dp[0][i - 1], dp[0][i - 2]) + sticker[1][i]
    print(max(dp[0][N], dp[1][N]))