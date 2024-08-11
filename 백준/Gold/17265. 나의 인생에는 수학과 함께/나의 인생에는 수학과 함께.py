import sys
input = sys.stdin.readline

N = int(input())
grid = [input().strip().split() for _ in range(N)]

dy = [1, 0]
dx = [0, 1]
min_value = float('inf')
max_value = float('-inf')

def solve(y, x, val):
    global min_value, max_value
    
    if y == N - 1 and x == N - 1:
        min_value = min(min_value, val)
        max_value = max(max_value, val)
        return

    for i in range(2):
        ny, nx = y + dy[i], x + dx[i]
        if ny >= N or nx >= N:
            continue
        
        next_val = val
        if grid[y][x] == '-':
            next_val -= int(grid[ny][nx])
        elif grid[y][x] == '+':
            next_val += int(grid[ny][nx])
        elif grid[y][x] == '*':
            next_val *= int(grid[ny][nx])
        
        solve(ny, nx, next_val)

solve(0, 0, int(grid[0][0]))

print(max_value, min_value)
