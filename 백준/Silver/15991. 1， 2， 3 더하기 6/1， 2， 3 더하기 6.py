import sys
input = sys.stdin.readline
mod = 10**9 + 9
max_dp = 50000

dp = [0] * (max_dp + 1)
dp[0], dp[1], dp[2] = 1, 1, 2
for i in range(3, max_dp + 1):
    dp[i] = (dp[i - 1] + dp[i - 2] + dp[i - 3]) % mod

T = int(input())
for _ in range(T):
    n = int(input())
    total = 0

    if n % 2 == 0:
        k = n // 2
        if k <= max_dp:
            total += dp[k]

    for m in [1, 2, 3]:
        rem = n - m
        if rem >= 0 and rem % 2 == 0:
            k = rem // 2
            if k <= max_dp:
                total += dp[k]

    print(total % mod)