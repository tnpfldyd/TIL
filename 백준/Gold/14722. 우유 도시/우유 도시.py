import sys
input = sys.stdin.readline

N = int(input())
milk_map = [list(map(int, input().split())) for _ in range(N)]
dp = [[[0, -1] for _ in range(N+1)] for _ in range(N+1)]

for row in range(1, N+1):
    for col in range(1, N+1):
        left, up = dp[row][col-1], dp[row-1][col]
        current_milk = milk_map[row-1][col-1]
        
        left_drinkable = (left[1]+1)%3 == current_milk
        up_drinkable = (up[1]+1)%3 == current_milk

        left_score = left[0] + left_drinkable
        up_score = up[0] + up_drinkable
        
        if left_score > up_score:
            dp[row][col][0] = left_score
            dp[row][col][1] = current_milk if left_drinkable else left[1]
        else:
            dp[row][col][0] = up_score
            dp[row][col][1] = current_milk if up_drinkable else up[1]

print(dp[N][N][0])