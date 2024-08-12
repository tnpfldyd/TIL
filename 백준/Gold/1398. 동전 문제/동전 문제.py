import sys
input = sys.stdin.readline
coins = [1, 10, 25]

for _ in range(int(input())):
    x = int(input())
    ans = 0
    dp = [10 ** 15 + 1] * 100
    dp[0] = 0
    for coin in coins:
        for i in range(coin, 100):
            dp[i] = min(dp[i], dp[i - coin]+1)
    while x:
        ans += dp[x % 100]
        x //= 100
    print(ans)