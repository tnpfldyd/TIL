import sys
input = sys.stdin.readline
MOD = 1234567

T = int(input())
for _ in range(T):
    n = int(input())
    counts = [1] * 10

    for _ in range(n - 1):
        prev = counts.copy()

        counts[0] = prev[7]
        counts[1] = prev[2] + prev[4]
        counts[2] = prev[1] + prev[3] + prev[5]
        counts[3] = prev[2] + prev[6]
        counts[4] = prev[1] + prev[5] + prev[7]
        counts[5] = prev[2] + prev[4] + prev[6] + prev[8]
        counts[6] = prev[3] + prev[5] + prev[9]
        counts[7] = prev[4] + prev[8] + prev[0]
        counts[8] = prev[5] + prev[7] + prev[9]
        counts[9] = prev[6] + prev[8]

        for i in range(10):
            counts[i] %= MOD

    print(sum(counts) % MOD)