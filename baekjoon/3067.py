import sys
input = sys.stdin.readline

for _ in range(int(input())):
    N = int(input())
    coins = tuple(map(int, input().split()))
    target = int(input())
    dp = [0] * (target + 1)
    dp[0] = 1

    for coin in coins:
        for i in range(coin, target + 1):
            dp[i] += dp[i - coin]
    
    print(dp[target])