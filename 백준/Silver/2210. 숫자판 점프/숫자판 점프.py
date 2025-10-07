import sys
input = sys.stdin.readline

board = [list(input().split()) for _ in range(5)]
numbers = set()

def dfs(r, c, num):
    if len(num) == 6:
        numbers.add(num)
        return
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if 0 <= nr < 5 and 0 <= nc < 5:
            dfs(nr, nc, num + board[nr][nc])

for i in range(5):
    for j in range(5):
        dfs(i, j, board[i][j])

print(len(numbers))