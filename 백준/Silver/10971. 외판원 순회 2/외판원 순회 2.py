import sys

def main():
    input = sys.stdin.readline
    n = int(input())
    W = [list(map(int, input().split())) for _ in range(n)]
    INF = 10**12
    full = (1 << n) - 1
    ans = INF

    for st in range(n):
        dp = [[INF] * n for _ in range(1 << n)]
        dp[1 << st][st] = 0
        for bit in range(1 << n):
            if not (bit & (1 << st)):
                continue
            for u in range(n):
                if not (bit & (1 << u)) or dp[bit][u] == INF:
                    continue
                for v in range(n):
                    if bit & (1 << v) or W[u][v] == 0:
                        continue
                    nb = bit | (1 << v)
                    cost = dp[bit][u] + W[u][v]
                    if cost < dp[nb][v]:
                        dp[nb][v] = cost
        for u in range(n):
            if u != st and W[u][st] != 0:
                total = dp[full][u] + W[u][st]
                if total < ans:
                    ans = total

    print(ans)

if __name__ == "__main__":
    main()