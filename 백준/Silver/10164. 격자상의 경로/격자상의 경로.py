n, m, k = map(int, input().split())

def find(n, m):
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == 1 and j == 1:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    return dp[n][m]

if k == 0:
    print(find(n, m))
else:
    dotN1 = (k - 1) // m + 1
    dotM1 = k - (dotN1 - 1) * m
    dotN2 = n - (dotN1 - 1)
    dotM2 = m - (dotM1 - 1)

    first = find(dotN1, dotM1)
    second = find(dotN2, dotM2)

    print(first * second)