import sys
input = sys.stdin.readline

H, W = map(int, input().split())
grid = []
for _ in range(H):
    grid.append(input().strip())

result = []
for i in range(H):
    row = []
    for j in range(W):
        if grid[i][j] == 'c':
            row.append(0)
        else:
            time = -1
            for k in range(j - 1, -1, -1):
                if grid[i][k] == 'c':
                    time = j - k
                    break
            row.append(time)
    result.append(row)

for row in result:
    print(*row)