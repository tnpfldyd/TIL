import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
dp = [sys.maxsize] * (n + 1)
dp[0] = 0

for i in range(n):
    for j in range(a[i]):
        if i + j + 1 < len(dp):
            dp[i + j + 1] = min(dp[i + j + 1], dp[i] + 1)

if dp[n - 1] < sys.maxsize:
    print(dp[n - 1])
else:
    print(-1)