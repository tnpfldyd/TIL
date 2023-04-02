N, K = map(int, input().split())

dp = [[0] * (N+1) for _ in range(N+1)]
dp[0][0] = 1
for r in range(1, N+1):
    for l in range(N+1):
        if l == 0:
            dp[l][r] = dp[l+1][r-1]
        elif l == N:
            dp[l][r] = dp[l-1][r-1]
        else:
            dp[l][r] = dp[l-1][r-1] + dp[l+1][r-1]

if dp[0][N] <= K:
    print(-1)
else:
    answer = ''
    left = 0
    right = 0
    for i in range(N):
        if left + 1 <= N and dp[left+1][N-i-1] > K:
            answer += '('
            left += 1
        else:
            answer += ')'
            K -= dp[left+1][N-i-1]
            left -= 1
    print(answer)