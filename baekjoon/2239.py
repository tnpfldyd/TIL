import sys
input = sys.stdin.readline

board = []
points = []
for i in range(9):
    row = list(map(int, list(input().strip())))
    for j in range(9):
        if not row[j]:
            points.append((i, j))
    board.append(row)

def isPossible(x, y):
    square_x = x // 3
    square_y = y // 3
    for i in range(9):
        if board[x][i] == board[x][y] and i != y:
            return False
        if board[i][y] == board[x][y] and i != x:
            return False
    for i in range(square_x * 3, square_x * 3 + 3):
        for j in range(square_y * 3, square_y * 3 + 3):
            if board[i][j] == board[x][y]:
                if i != x and i != y:
                    return False
    return True

def sudoku(n):
    if n == cnt:
        for row in board:
            print(''.join(map(str, row)))
        sys.exit(0)
    x, y = points[n]
    for i in range(1, 10):
        board[x][y] = i
        if isPossible(x, y):
            sudoku(n + 1)
    board[x][y] = 0
cnt = len(points)
sudoku(0)
