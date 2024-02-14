import sys
input = sys.stdin.readline
INF = sys.maxsize

N, M = map(int, input().split())
prefix_sum = [[0] * (M + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    row = list(map(int, input().split()))
    for j in range(1, M + 1):
        prefix_sum[i][j] = row[j - 1] + prefix_sum[i][j - 1] + prefix_sum[i - 1][j] - prefix_sum[i - 1][j - 1]

answer = -INF
for i in range(1, N + 1):
    for j in range(1, M + 1):
        for ii in range(i):
            for jj in range(j):
                answer = max(answer, prefix_sum[i][j] - prefix_sum[ii][j] - prefix_sum[i][jj] + prefix_sum[ii][jj])

print(answer)