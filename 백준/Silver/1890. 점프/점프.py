import sys
input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
m = len(board[0])
dp = [[0] * m for _ in range(n)]
dp[0][0] = 1

def count_paths():
    for i in range(n):
        for j in range(m):
            step = board[i][j]
            if step == 0 or dp[i][j] == 0:
                continue
            if i + step < n:
                dp[i + step][j] += dp[i][j]
            if j + step < m:
                dp[i][j + step] += dp[i][j]
    return dp[-1][-1]

print(count_paths())