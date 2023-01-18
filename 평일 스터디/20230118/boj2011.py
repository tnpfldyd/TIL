import sys
sys.setrecursionlimit(10 ** 6)
numbers = input()
dp = [-1] * len(numbers)

def dfs(node):
    if node == len(numbers):
        return 1
    if dp[node] != -1:
        return dp[node]
    dp[node] = 0
    if numbers[node] != '0':
        dp[node] += dfs(node + 1)
        if node + 1 < len(numbers) and int(numbers[node : node+2]) <= 26:
            dp[node] += dfs(node + 2)
    return dp[node] % 1000000

print(dfs(0))