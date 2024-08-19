import sys
input = sys.stdin.readline

while True:
    N, M = map(int, input().split())
    if N == 0 and M == 0:
        break
    
    square = [list(map(int, input().split())) for _ in range(N)]
    dp = [[0] * (M + 1) for _ in range(N + 1)]

    max_length = 0
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            if square[i - 1][j - 1]:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                max_length = max(max_length, dp[i][j])
    
    print(max_length)