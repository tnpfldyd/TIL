N = int(input())
numbers = list(map(int, input().split()))
dp = [0] * N
answer = 0
for i in range(N):
    dp[i] = numbers[i]
    for j in range(i):
        if numbers[i] > numbers[j]:
            dp[i] = max(dp[i], dp[j] + numbers[i])
    answer = max(answer, dp[i])
print(answer)