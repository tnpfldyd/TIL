import sys
input = sys.stdin.readline

n, m = map(int, input().split())
baskets = []

for _ in range(n):
    x, y = map(int, input().split())
    if x + y <= m:
        baskets.append((x, y))

baskets.sort()
dp = []

for i in range(len(baskets)):
    x_i, y_i = baskets[i]
    current = max(0, m - (x_i + y_i))
    max_val = current
    for j in range(i):
        x_j, y_j = baskets[j]
        if x_j <= x_i and y_j <= y_i:
            if dp[j] + current > max_val:
                max_val = dp[j] + current
    dp.append(max_val)

print(max(dp) if dp else 0)