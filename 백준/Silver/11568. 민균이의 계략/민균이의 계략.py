from bisect import bisect_left

N = int(input())
arr = list(map(int, input().split()))

dp = []

for num in arr:
    pos = bisect_left(dp, num)
    if pos == len(dp):
        dp.append(num)
    else:
        dp[pos] = num

print(len(dp))