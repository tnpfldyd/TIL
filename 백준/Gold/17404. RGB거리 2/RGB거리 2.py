import sys
input = sys.stdin.readline
N = int(input())
rgb_list = [[0,0,0]]+[list(map(int,input().strip().split())) for _ in range(N)]
dp = [[0] * 3 for _ in range(N+1)]
answer = 1000001
for i in range(3):
    for j in range(3):
        if i == j:
            dp[1][j] = rgb_list[1][j]
        else:
            dp[1][j] = 1000001
    for j in range(2, N+1):
        for k in range(3):
            dp[j][k] = min(dp[j-1][(k+1)%3], dp[j-1][(k+2)%3]) + rgb_list[j][k]
    for j in range(3):
        if i == j:
            continue
        answer = min(answer, dp[N][j])
print(answer)