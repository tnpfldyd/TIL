import sys
input = sys.stdin.readline

N, M = map(int, input().split())

dp = [1] * (1 << M)

for _ in range(1, N):
    new_dp = [0] * (1 << M)
    for prev in range(1 << M):
        if dp[prev] == 0:
            continue
        for curr in range(1 << M):
            overlap = prev & curr
            if (overlap & (overlap >> 1)) == 0:
                new_dp[curr] += dp[prev]
    dp = new_dp

print(sum(dp))