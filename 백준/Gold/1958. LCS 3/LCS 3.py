A, B, C = input(), input(), input()
dp = [[[0] * (len(C) + 1) for _ in range(len(B) + 1)] for _ in range(len(A) + 1)]

for i in range(1, len(A) + 1):
    for j in range(1, len(B) + 1):
        for k in range(1, len(C) + 1):
            a, b, c = A[i - 1], B[j - 1], C[k - 1]
            if a == b and b == c:
                dp[i][j][k] = dp[i - 1][j - 1][k - 1] + 1
            else:
                dp[i][j][k] = max(dp[i - 1][j][k], dp[i][j - 1][k], dp[i][j][k - 1])

print(dp[-1][-1][-1])