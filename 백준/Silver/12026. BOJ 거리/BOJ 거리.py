import sys

input = sys.stdin.readline

INF = float('inf')
n = int(input())
blocks = input().strip()
dp = [INF] * n
dp[0] = 0

prev_map = {'O': 'B', 'J': 'O', 'B': 'J'}

for i in range(1, n):
    for j in range(i):
        if blocks[j] == prev_map[blocks[i]]:
            dp[i] = min(dp[i], dp[j] + (i - j) ** 2)

print(dp[-1] if dp[-1] != INF else -1)