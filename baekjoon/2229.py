N = int(input())
students = list(map(int, input().split()))
dp = [0] * (N + 1)

for i in range(1, N + 1):
    for j in range(i, 0, -1):
        a, b = students[i - 1], students[j - 1]
        maxStudent = max(a, b)
        minStudent = min(a, b)

        dp[i] = max(dp[i], dp[j-1] + maxStudent - minStudent)

print(dp[N])
