import sys
input = sys.stdin.readline

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

for i in range(1, n):
    for j in range(m):
        grid[i][j] += grid[i - 1][j]

for _ in range(int(input())):
    x1, y1, x2, y2 = map(int, input().split())
    result = sum(grid[x2 - 1][y1 - 1:y2])
    if x1 > 1:
        result -= sum(grid[x1 - 2][y1 - 1:y2])
    print(result)