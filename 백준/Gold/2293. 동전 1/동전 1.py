import sys
input = sys.stdin.readline
N, target = map(int, input().split())
coins = [0]
for _ in range(N):
    coin = int(input())
    coins.append(coin)
dp = [0] * (target + 1)
dp[0] = 1
for i in range(1, N + 1):
    for j in range(coins[i], target + 1):
        dp[j] += dp[j - coins[i]]
print(dp[target])