import sys
input = sys.stdin.readline
N = int(input())
dp = [0] * (N + 1)
max_length = 0
numbers = [0] + list(map(int, input().split()))
for i in range(1, N + 1):
    k = numbers[i]
    dp[k] = dp[k - 1] + 1
    max_length = max(max_length, dp[k])

print(N - max_length)