N = int(input())
numbers = [0] + list(map(int, input().split()))
prefix_sum = [0] * 100010

for i in range(1, N + 1):
    prefix_sum[i] = prefix_sum[i - 1] + numbers[i]
target = 0
result = 0
dp = [0] * 5

if prefix_sum[N] % 4 > 0:
    result = 0
else:
    if prefix_sum[N] == 0:
        zero_count = sum(1 for i in range(1, N + 1) if prefix_sum[i] == 0)
        result = (zero_count - 1) * (zero_count - 2) * (zero_count - 3) // 6
    else:
        dp[0] = 1
        target = prefix_sum[N] // 4

        for i in range(1, N + 1):
            quarter = prefix_sum[i] // target
            if prefix_sum[i] % target != 0 or quarter < 1 or quarter > 4:
                continue

            dp[quarter] += dp[quarter - 1]

        result = dp[4]

print(result)