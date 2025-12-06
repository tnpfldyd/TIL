from copy import deepcopy
import sys
input = sys.stdin.readline

dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

board = [list(map(int, input().split())) for _ in range(5)]
r, c = map(int, input().split())

answer = 0

def dfs(brd, x, y, moves, apples):
    global answer
    if apples >= 2:
        answer = 1
        return
    if moves == 3:
        return
    for dx, dy in dirs:
        nx, ny = x + dx, y + dy
        if not (0 <= nx < 5 and 0 <= ny < 5):
            continue
        if brd[nx][ny] == -1:
            continue
        new_board = deepcopy(brd)
        new_apples = apples + (1 if new_board[nx][ny] == 1 else 0)
        new_board[x][y] = -1
        dfs(new_board, nx, ny, moves + 1, new_apples)
        if answer == 1:
            return

dfs(board, r, c, 0, 0)
print(answer)