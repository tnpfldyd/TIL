import sys
input = sys.stdin.readline

n, m = map(int, input().split())
grid = [input().strip() for _ in range(n)]

max_size = 1

for i in range(n):
    for j in range(m):
        max_possible = min(n - i, m - j)
        
        for size in range(2, max_possible + 1):
            if (grid[i][j] == grid[i][j + size - 1] == 
                grid[i + size - 1][j] == grid[i + size - 1][j + size - 1]):
                max_size = max(max_size, size)

print(max_size * max_size)