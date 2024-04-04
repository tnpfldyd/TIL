numbers = list(map(int, input().split()))[:-1]
N = len(numbers)
dp = [[[float('inf')] * 5 for _ in range(5)] for _ in range(N + 1)]

dp[0][0][0] = 0

def power(cur, nxt):
    if cur == nxt:
        return 1
    elif not cur:
        return 2
    elif abs(cur - nxt) == 1 or abs(cur - nxt) == 3:
        return 3
    else:
        return 4

for i in range(N):
    nxt = numbers[i]
    for j in range(5):
        for k in range(5):
            if dp[i][j][k] == float('inf'):
                continue

            dp[i + 1][nxt][k] = min(dp[i + 1][nxt][k], dp[i][j][k] + power(j, nxt))
            dp[i + 1][j][nxt] = min(dp[i + 1][j][nxt], dp[i][j][k] + power(k, nxt))

answer = float('inf')
for j in range(5):
    for k in range(5):
        answer = min(answer, dp[N][j][k])

print(answer)