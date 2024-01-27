N = int(input())
numbers = list(map(int, input().split()))
dp = [[0] * N for _ in range(2)]

dp[0][0] = dp[1][0] = numbers[0]
answer = numbers[0]
for i in range(1, N):
    current = numbers[i]
    dp[0][i] = max(dp[0][i - 1] + current, current)
    dp[1][i] = max(dp[0][i - 1], dp[1][i - 1] + current)
    answer = max(answer, dp[0][i], dp[1][i])
print(answer)