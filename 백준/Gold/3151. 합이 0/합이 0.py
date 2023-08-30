N = int(input())
numbers = list(map(int, input().split()))
dp = [0] * 30001
answer = 0
for i in range(1, N):
    answer += dp[10000 - numbers[i]]
    for j in range(i):
        dp[10000 + numbers[i] + numbers[j]] += 1

print(answer)