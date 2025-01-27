import sys
input = sys.stdin.readline

N = int(input())
arr = [0] + list(map(int, input().split()))

dp = [0] * (max(arr) + 1)

for num in arr[1:]:
    dp[num] = max(dp[num], dp[num - 1] + 1)

print(max(dp))