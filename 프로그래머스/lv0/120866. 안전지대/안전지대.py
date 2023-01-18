def solution(board):
    dx, dy = [0,0,1,-1,1,1,-1,-1], [1,-1,0,0,1,-1,1,-1]
    N = len(board)
    temp = []
    cnt = set()
    for i in range(N):
        for j in range(N):
            if board[i][j]:
                temp.append((i, j))
                cnt.add((i, j))
    for x, y in temp:
        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                board[nx][ny] = 1
                cnt.add((nx, ny))
    answer = N*N - len(cnt)
    return answer