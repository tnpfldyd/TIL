N = int(input())
numbers = list(map(int, input().split()))
dp = [0] * 1001
answer = 0
for number in numbers:
    dp[number] = max(dp[:number]) + number
    answer = max(answer, dp[number])
print(answer)