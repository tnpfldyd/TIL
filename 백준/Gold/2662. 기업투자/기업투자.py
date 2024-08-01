import sys
input = sys.stdin.readline

N, M = map(int, input().split())
investment_profit = [[0] * (M + 1)]

for _ in range(N):
    investment_profit.append(list(map(int, input().split())))

max_profit = [[0] * (M + 1) for _ in range(N + 1)]
track = [[[0] * (M + 1) for _ in range(M + 1)] for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, M + 1):
        max_profit[i][j] = max(max_profit[i][j - 1], investment_profit[i][j])
        if max_profit[i][j] == investment_profit[i][j]:
            track[i][j][j] = i
        else:
            track[i][j] = track[i][j - 1].copy()

        for k in range(1, i+1):
            if max_profit[i][j] < max_profit[k][j - 1] + investment_profit[i - k][j]:
                max_profit[i][j] = max_profit[k][j - 1] + investment_profit[i - k][j]
                track[i][j] = track[k][j - 1].copy()
                track[i][j][j] = i - k

print(max_profit[-1][-1])
print(*track[-1][-1][1:])
