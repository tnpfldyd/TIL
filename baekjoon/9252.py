N = 1001

def back(i, j):
    if dp[i][j] == 0:
        return
    if a[i-1] == b[j-1]:
        back(i-1, j-1)
        print(a[i-1], end='')
    else:
        back(i-1, j) if dp[i-1][j] > dp[i][j-1] else back(i, j-1)

a = input()
b = input()

dp = [[0] * N for _ in range(N)]

for i in range(len(a)):
    for j in range(len(b)):
        dp[i+1][j+1] = dp[i][j] + 1 if a[i] == b[j] else max(dp[i][j+1], dp[i+1][j])

print(dp[len(a)][len(b)])
back(len(a), len(b))