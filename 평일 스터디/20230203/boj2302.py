N, M = int(input()), int(input())

dp = [0] * 41
dp[1], dp[2], dp[3], dp[4] = 1, 2, 3, 5
for i in range(5, N+1):
    dp[i] = dp[i-1] + dp[i-2]
visited = [False] * (N + 1)
for _ in range(M):
    visited[int(input())] = True
cnt = 0
result = 1
for i in range(1, N+1):
    if not visited[i]:
        cnt += 1
    else:
        if cnt:
            result *= dp[cnt]
            cnt = 0
if cnt:
    result *= dp[cnt]

print(result)