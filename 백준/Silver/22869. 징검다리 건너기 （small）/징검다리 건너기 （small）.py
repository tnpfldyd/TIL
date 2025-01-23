n, k = map(int, input().split())
stone = list(map(int, input().split()))
dp = [0] * n
dp[0] = 1

for i in range(n - 1):
    for j in range(i + 1, n):
        if dp[i] and (j - i) * (1 + abs(stone[j] - stone[i])) <= k:
        	dp[j] = 1

print("YES" if dp[n - 1] else "NO")