import sys
input = sys.stdin.readline

n = int(input())
grades = [(0, 0)]
for _ in range(n):
    a, b = map(int, input().split())
    grades.append((a, b))

dp = [[[0, 0] for _ in range(2)] for _ in range(n + 1)]
result = [0, 5]

for i in range(1, n + 1):
    for j in range(2):
        dp[i][j][1] = grades[i][j]
        for k in range(2):
            if grades[i][j] == dp[i - 1][k][1]:
                dp[i][j][0] = dp[i - 1][k][0]
                break
        dp[i][j][0] += 1
        
        if result[0] < dp[i][j][0]:
            result = [dp[i][j][0], dp[i][j][1]]
        elif result[0] == dp[i][j][0] and result[1] > dp[i][j][1]:
            result[1] = dp[i][j][1]

print(*result)