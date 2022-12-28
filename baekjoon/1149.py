import sys
input = sys.stdin.readline
N = int(input())
rgb_list = [[0,0,0]]+[list(map(int,input().strip().split())) for _ in range(N)]
dp = [[0] * 3 for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(3):
        dp[i][j] = min(dp[i-1][(j+1)%3], dp[i-1][(j+2)%3]) + rgb_list[i][j]
print(min(dp[N]))
