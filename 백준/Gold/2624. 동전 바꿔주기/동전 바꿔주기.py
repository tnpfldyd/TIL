import sys
input = sys.stdin.readline

def solve(total, idx):
    if total == 0:
        dp[total][idx] = 1
        return 1
    if idx > k:
        dp[total][idx] = 0
        return 0

    if dp[total][idx] != -1:
        return dp[total][idx]

    result = 0

    for i in range(coins[idx][1] + 1):
        if total - (coins[idx][0] * i) >= 0:
            result += solve(total - (coins[idx][0] * i), idx + 1)

    dp[total][idx] = result
    return result

T = int(input())
k = int(input())

coins = [(0, 0)] * (k + 1)
dp = [[-1] * (k + 2) for _ in range(T + 1)]

for i in range(1, k + 1):
    p, n = map(int, input().split())
    coins[i] = (p, n)

print(solve(T, 1))