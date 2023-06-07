import sys
input = sys.stdin.readline
N = int(input())
MAP = [[0] * (N + 1) for _ in range(N + 1)]
DP = [[0] * (N + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    MAP[i][1:N + 1] = list(map(int, input().split()))
for i in range(1, N + 1):
    for j in range(1, N + 1):
        Cost1 = 0
        Cost2 = 0
        if j > 1:
            Cost1 = 0 if MAP[i][j] < MAP[i][j - 1] else MAP[i][j] - MAP[i][j - 1] + 1
        if i > 1:
            Cost2 = 0 if MAP[i][j] < MAP[i - 1][j] else MAP[i][j] - MAP[i - 1][j] + 1
        if i == 1:
            DP[i][j] = DP[i][j - 1] + Cost1
        elif j == 1:
            DP[i][j] = DP[i - 1][j] + Cost2
        else:
            DP[i][j] = min(DP[i][j - 1] + Cost1, DP[i - 1][j] + Cost2)

print(DP[N][N])