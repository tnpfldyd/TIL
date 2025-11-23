import sys
input = sys.stdin.readline

C = int(input())
for _ in range(C):
    a = [list(map(int, input().split())) for _ in range(11)]
    dp = [-1] * (1 << 11)
    dp[0] = 0

    for mask in range(1 << 11):
        if dp[mask] < 0:
            continue
        player = bin(mask).count("1")
        for pos in range(11):
            if mask & (1 << pos) == 0 and a[player][pos] > 0:
                nxt = mask | (1 << pos)
                val = dp[mask] + a[player][pos]
                if val > dp[nxt]:
                    dp[nxt] = val

    print(dp[(1 << 11) - 1])