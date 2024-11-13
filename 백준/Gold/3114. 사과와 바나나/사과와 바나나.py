import sys
input = sys.stdin.readline
def sum_ba_ap(x, y):
    return psum1[y][x - 1] + psum2[y][r] - psum2[y][x]

r, c = map(int, input().split())
ba = [[0] * (c + 1) for _ in range(r + 1)]
ap = [[0] * (c + 1) for _ in range(r + 1)]
psum1 = [[0] * (r + 1) for _ in range(c + 1)]
psum2 = [[0] * (r + 1) for _ in range(c + 1)]
dp = [[0] * (c + 1) for _ in range(r + 1)]



for i in range(1, r + 1):
    row = input().split()
    for j in range(1, c + 1):
        x, n = row[j - 1][0], int(row[j - 1][1:])
        if x == 'B':
            ba[i][j] = n
        else:
            ap[i][j] = n

for j in range(1, c + 1):
    for i in range(1, r + 1):
        psum1[j][i] = psum1[j][i - 1] + ba[i][j]
        psum2[j][i] = psum2[j][i - 1] + ap[i][j]

for i in range(1, r + 1):
    dp[i][1] = psum2[1][r] - psum2[1][i]

for j in range(2, c + 1):
    dp[1][j] = dp[1][j - 1] + psum2[j][r] - psum2[j][1]

for i in range(2, r + 1):
    for j in range(2, c + 1):
        dp[i][j] = max(dp[i][j - 1], dp[i - 1][j - 1]) + sum_ba_ap(i, j)
        dp[i][j] = max(dp[i][j], dp[i - 1][j] - ap[i][j])

print(dp[r][c])