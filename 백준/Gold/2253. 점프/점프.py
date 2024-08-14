import sys
input = sys.stdin.readline

N, stone_n = map(int, input().split())

stone = set(int(input()) for _ in range(stone_n))

MAX_VALUE = 10001
MAX_JUMP = int((2 * N) ** 0.5) + 2
dp = [[MAX_VALUE] * MAX_JUMP for _ in range(N + 1)]

dp[1][0] = 0

for i in range(2, N + 1):
    if i in stone:
        continue
    
    for v in range(1, int((2 * i) ** 0.5) + 1):
        dp[i][v] = min(dp[i - v][v - 1], dp[i - v][v], dp[i - v][v + 1]) + 1

ans = min(dp[N])
if ans == MAX_VALUE:
    print(-1)
else:
    print(ans)