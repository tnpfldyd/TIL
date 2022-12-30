import sys
input = sys.stdin.readline

N = int(input())
matrix = [list(map(int, input().strip().split())) for _ in range(N)]
W_B = [0, 0]
def solve(x, y, n):
    cnt = 0
    for i in range(x, x+n):
        for j in range(y, y+n):
            if matrix[i][j]:
                cnt += 1
    if cnt == n*n:
        W_B[1] += 1
    elif not cnt:
        W_B[0] += 1
    else:
        solve(x, y, n//2) # left top
        solve(x, y + (n//2), n//2) # right top
        solve(x + (n//2), y, n//2) # left bottom
        solve(x + (n//2), y + (n//2), n//2) # right bottom
    return
solve(0, 0, N)
for i in W_B:
    print(i)