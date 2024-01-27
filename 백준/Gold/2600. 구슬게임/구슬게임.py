import sys
input = sys.stdin.readline

def memoization(a, b):
    if dp[a][b] >= 0:
        return dp[a][b]

    for i in range(3):
        if balls[i] <= a and not memoization(a - balls[i], b):
            dp[a][b] = 1
            return True

    for i in range(3):
        if balls[i] <= b and not memoization(a, b - balls[i]):
            dp[a][b] = 1
            return True

    dp[a][b] = 0
    return False

dp = [[-1] * 501 for _ in range(501)]
balls = list(map(int, input().split()))
for _ in range(5):
    k1, k2 = map(int, input().split())
    print('A' if memoization(k1, k2) else 'B')