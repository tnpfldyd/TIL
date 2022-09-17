def solution(m, n, board):
    new_board = []
    for i in board:
        temp = []
        for j in i:
            temp.append(j)
        new_board.append(temp)
    dx, dy = [0,1,1,0], [1,0,1,0]
    final = 0
    while True:
        zero = set()
        for i in range(m):
            for j in range(n):
                if new_board[i][j] != 0:
                    cnt = 0
                    for k in range(3):
                        ni, nj = i + dx[k], j + dy[k]
                        if 0 <= ni < m and 0 <= nj < n:
                            if new_board[i][j] == new_board[ni][nj]:
                                cnt += 1
                    if cnt == 3:
                        for k in range(4):
                            ni, nj = i + dx[k], j + dy[k]
                            zero.add((ni, nj))
        if len(zero) == 0:
            break
        for k,v in zero:
            new_board[k][v] = 0
        for i in range(m-1, -1, -1):
            for j in range(n):
                if new_board[i][j] == 0:
                    temp = i - 1
                    while temp >= 0 and new_board[temp][j] == 0:
                        temp -= 1
                    if temp < 0:
                        new_board[i][j] = 0
                    else:
                        new_board[i][j] = new_board[temp][j]
                        new_board[temp][j] = 0
    for i in range(m):
        for j in range(n):
            if new_board[i][j] == 0:
                final += 1
    return final