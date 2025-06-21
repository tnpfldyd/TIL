import sys
input = sys.stdin.readline

N, M, x, y, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
cmds = list(map(int, input().split()))

dice = [0] * 7
top, bot, north, south, east, west = 1, 6, 2, 5, 3, 4

for c in cmds:
    if c == 1:
        nx, ny = x, y + 1
        if ny >= M: continue
        top, bot, east, west = west, east, top, bot
    elif c == 2:
        nx, ny = x, y - 1
        if ny < 0: continue
        top, bot, east, west = east, west, bot, top
    elif c == 3:
        nx, ny = x - 1, y
        if nx < 0: continue
        top, bot, north, south = south, north, top, bot
    else:
        nx, ny = x + 1, y
        if nx >= N: continue
        top, bot, north, south = north, south, bot, top

    x, y = nx, ny

    if board[x][y] == 0:
        board[x][y] = dice[bot]
    else:
        dice[bot] = board[x][y]
        board[x][y] = 0

    print(dice[top])