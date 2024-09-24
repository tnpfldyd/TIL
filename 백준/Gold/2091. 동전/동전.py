import sys
input = sys.stdin.readline

sys.setrecursionlimit(10**9)

def dfs(current_sum, coin_count):
    if memo[current_sum] >= coin_count:
        return
    if current_sum == target:
        memo[current_sum] = coin_count
        for i in range(4):
            result[i] = used_coins[i]
        return
    memo[current_sum] = coin_count
    if available_coins[0] >= used_coins[0] + 5 and current_sum + 5 <= target:
        used_coins[0] += 5
        dfs(current_sum + 5, coin_count + 5)
        used_coins[0] -= 5
    if available_coins[1] > used_coins[1] and current_sum + 5 <= target:
        used_coins[1] += 1
        dfs(current_sum + 5, coin_count + 1)
        used_coins[1] -= 1
    if available_coins[2] > used_coins[2] and current_sum + 10 <= target:
        used_coins[2] += 1
        dfs(current_sum + 10, coin_count + 1)
        used_coins[2] -= 1
    if available_coins[3] > used_coins[3] and current_sum + 25 <= target:
        used_coins[3] += 1
        dfs(current_sum + 25, coin_count + 1)
        used_coins[3] -= 1

if __name__ == '__main__':
    result = [0] * 4
    memo = [0] * 10001
    used_coins = [0] * 4

    target, *available_coins = map(int, input().split())

    remainder = target % 5
    if available_coins[0] < remainder:
        print(0, 0, 0, 0)
        exit(0)
    for i in range(target + 1):
        memo[i] = -1
    used_coins[0], current_sum = remainder, remainder
    dfs(current_sum, current_sum)

    for coin_count in result:
        print(coin_count, end=' ')