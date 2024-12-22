import sys
input = sys.stdin.readline

dp = [0] * 251
dp[0], dp[1], dp[2] = 1, 1, 3

while True:
    try:
        n = int(input())
        for i in range(3, n + 1):
            if not dp[i]:
                dp[i] = dp[i - 1] + 2 * dp[i - 2]
        print(dp[n])
    except:
        break