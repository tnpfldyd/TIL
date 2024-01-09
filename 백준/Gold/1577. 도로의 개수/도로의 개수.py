from collections import deque
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
dx, dy = [0, 1], [1, 0]
q = deque()
q.append((0, 0))
prohibited_area = set()
for _ in range(int(input())):
    sx, sy, ex, ey = map(int, input().split())
    prohibited_area.add((sx, sy, ex, ey))
    prohibited_area.add((ex, ey, sx, sy))
dp = [[0] * (M + 1) for _ in range(N + 1)]
dp[0][0] = 1

for y in range(M + 1):
    for x in range(N + 1):
        if x and (x - 1, y, x, y) not in prohibited_area:
            dp[x][y] += dp[x - 1][y]
        if y and (x, y - 1, x, y) not in prohibited_area:
            dp[x][y] += dp[x][y - 1]
print(dp[N][M])