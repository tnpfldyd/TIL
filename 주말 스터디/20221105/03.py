from collections import deque
matrix = ['..XXX', '..XXX', '...XX', 'X....', 'XXX..']
N = len(matrix); M = len(matrix[0])
start = deque()
start.append((0, 0, 0))
visited = [[[-1] * 8 for _ in range(M)] for _ in range(N)]
# 0 = 우 1 = 우하 2 = 하 3 = 좌하 4 = 좌 5 = 좌상 6 = 상 7 = 우상
visited[0][0][0] = 0
while start:
    x, y, dir = start.popleft()
    if x == N-1 and y == M-1:
        print(visited[x][y][dir])
        break
    if dir == 0:
        nx1, ny1, nx2, ny2, nx3, ny3 = x, y+1, x-1, y+1, x+1, y+1
        if 0 <= nx1 < N and 0 <= ny1 < M:
            if matrix[nx1][ny1] == '.' and visited[nx1][ny1][dir] == -1:
                visited[nx1][ny1][dir] = visited[x][y][dir] + 1
                start.append((nx1, ny1, dir))
        if 0 <= nx2 < N and 0 <= ny2 < M: #우상
            if matrix[nx2][ny2] == '.' and matrix[nx2][ny2-1] == '.' and matrix[nx2+1][ny2] == '.' and visited[nx2][ny2][7] == -1:
                visited[nx2][ny2][7] = visited[x][y][dir] + 1
                start.append((nx2, ny2, 7))
        if 0 <= nx3 < N and 0 <= ny3 < M: #우하
            if matrix[nx3][ny3] == '.' and matrix[nx3-1][ny3] == '.' and matrix[nx3][ny3-1] == '.' and visited[nx3][ny3][1] == -1:
                visited[nx3][ny3][1] = visited[x][y][dir] + 1
                start.append((nx3, ny3, 1))
    elif dir == 1:
        nx1, ny1, nx2, ny2, nx3, ny3 = x+1, y+1, x+1, y, x, y+1
        if 0 <= nx1 < N and 0 <= ny1 < M:
            if matrix[nx1][ny1] == '.' and matrix[nx1-1][ny1] == '.' and matrix[nx1][ny1-1] == '.' and visited[nx1][ny1][1] == -1:
                visited[nx1][ny1][1] = visited[x][y][dir] + 1
                start.append((nx1, ny1, 1))
        if 0 <= nx2 < N and 0 <= ny2 < M:
            if matrix[nx2][ny2] == '.' and visited[nx2][ny2][2] == -1:
                visited[nx2][ny2][2] = visited[x][y][dir] + 1
                start.append((nx2, ny2, 2))
        if 0 <= nx3 < N and 0 <= ny3 < M:
            if matrix[nx3][ny3] == '.' and visited[nx3][ny3][0] == -1:
                visited[nx3][ny3][0] = visited[x][y][dir] + 1
                start.append((nx3, ny3, 0))
    elif dir == 2:
        nx1, ny1, nx2, ny2, nx3, ny3 = x+1, y, x+1, y+1, x+1, y-1 # 하 우하 좌하
        if 0 <= nx1 < N and 0 <= ny1 < M:
            if matrix[nx1][ny1] == '.' and visited[nx1][ny1][dir] == -1:
                visited[nx1][ny1][dir] = visited[x][y][dir] + 1
                start.append((nx1, ny1, 2))
        if 0 <= nx2 < N and 0 <= ny2 < M:
            if matrix[nx2][ny2] == '.' and matrix[nx2-1][ny2] == '.' and matrix[nx2][ny2-1] == '.' and visited[nx2][ny2][1] == -1:
                visited[nx2][ny2][1] = visited[x][y][dir] + 1
                start.append((nx2, ny2, 1))
        if 0 <= nx3 < N and 0 <= ny3 < M:
            if matrix[nx3][ny3] == '.' and matrix[nx3-1][ny3] == '.' and matrix[nx3][ny3+1] == '.' and visited[nx3][ny3][3] == -1:
                visited[nx3][ny3][3] = visited[x][y][dir] + 1
                start.append((nx3, ny3, 3))
    elif dir == 3: #좌하
        nx1, ny1, nx2, ny2, nx3, ny3 = x+1, y-1, x, y-1, x+1, y # 좌하, 좌, 하
        if 0 <= nx1 < N and 0 <= ny1 < M:
            if matrix[nx1][ny1] == '.' and matrix[nx1-1][ny1] == '.' and matrix[nx1][ny1+1] == '.' and visited[nx1][ny1][3] == -1:
                visited[nx1][ny1][3] = visited[x][y][dir] + 1
                start.append((nx1, ny1, 3))
        if 0 <= nx2 < N and 0 <= ny2 < M:
            if matrix[nx2][ny2] == '.' and visited[nx2][ny2][4] == -1:
                visited[nx2][ny2][4] = visited[x][y][dir] + 1
                start.append((nx2, ny2, 4))
        if 0 <= nx3 < N and 0 <= ny3 < M:
            if matrix[nx3][ny3] == '.' and visited[nx3][ny3][2] == -1:
                visited[nx3][ny3][2] = visited[x][y][dir] + 1
                start.append((nx3, ny3, 2))
    elif dir == 4: #좌
        nx1, ny1, nx2, ny2, nx3, ny3 = x, y-1, x+1, y-1, x-1, y-1 # 좌, 좌하, 좌상
        if 0 <= nx1 < N and 0 <= ny1 < M:
            if matrix[nx1][ny1] == '.' and visited[nx1][ny1][4] == -1:
                visited[nx1][ny1][4] = visited[x][y][dir] + 1
                start.append((nx1, ny1, 4))
        if 0 <= nx2 < N and 0 <= ny2 < M:
            if matrix[nx2][ny2] == '.' and matrix[nx2-1][ny2] == '.' and matrix[nx2][ny2+1] == '.' and visited[nx2][ny2][3] == -1:
                visited[nx2][ny2][3] = visited[x][y][dir] + 1
                start.append((nx2, ny2, 3))
        if 0 <= nx3 < N and 0 <= ny3 < M:
            if matrix[nx3][ny3] == '.' and matrix[nx3+1][ny3] == '.' and matrix[nx3][ny3+1] == '.' and visited[nx3][ny3][5] == -1:
                visited[nx3][ny3][5] = visited[x][y][dir] + 1
                start.append((nx3, ny3, 5))
    elif dir == 5: #좌상
        nx1, ny1, nx2, ny2, nx3, ny3 = x-1, y-1, x-1, y, x, y-1 #좌상 상 좌
        if 0 <= nx1 < N and 0 <= ny1 < M:
            if matrix[nx1][ny1] == '.' and matrix[nx1+1][ny1] == '.' and matrix[nx1][ny1+1] == '.' and visited[nx1][ny1][5] == -1:
                visited[nx1][ny1][5] = visited[x][y][dir] + 1
                start.append((nx1, ny1, 5))
        if 0 <= nx2 < N and 0 <= ny2 < M:
            if matrix[nx2][ny2] == '.' and visited[nx2][ny2][6] == -1:
                visited[nx2][ny2][6] = visited[x][y][dir] + 1
                start.append((nx2, ny2, 6))
        if 0 <= nx3 < N and 0 <= ny3 < M:
            if matrix[nx3][ny3] == '.' and visited[nx3][ny3][4] == -1:
                visited[nx3][ny3][4] = visited[x][y][dir] + 1
                start.append((nx3, ny3, 4))
    elif dir == 6: # 상
        nx1, ny1, nx2, ny2, nx3, ny3 = x-1, y, x-1, y-1, x-1, y+1 # 상 좌상 우상
        if 0 <= nx1 < N and 0 <= ny1 < M:
            if matrix[nx1][ny1] == '.' and visited[nx1][ny1][dir] == -1:
                visited[nx1][ny1][dir] = visited[x][y][dir] + 1
                start.append((nx1, ny1, 6))
        if 0 <= nx2 < N and 0 <= ny2 < M:
            if matrix[nx2][ny2] == '.' and matrix[nx2+1][ny2] == '.' and matrix[nx2][ny2+1] == '.' and visited[nx2][ny2][5] == -1:
                visited[nx2][ny2][5] = visited[x][y][dir] + 1
                start.append((nx2, ny2, 5))
        if 0 <= nx3 < N and 0 <= ny3 < M:
            if matrix[nx3][ny3] == '.' and matrix[nx3][ny3-1] == '.' and matrix[nx3+1][ny3] == '.' and visited[nx3][ny3][7] == -1:
                visited[nx3][ny3][7] = visited[x][y][dir] + 1
                start.append((nx3, ny3, 7))
    elif dir == 7: # 우상
        nx1, ny1, nx2, ny2, nx3, ny3 = x-1, y+1, x-1, y, x, y+1 # 우상 상 우
        if 0 <= nx1 < N and 0 <= ny1 < M:
            if matrix[nx1][ny1] == '.' and matrix[nx1][ny1-1] == '.' and matrix[nx1+1][ny1] == '.' and visited[nx1][ny1][7] == -1:
                visited[nx1][ny1][7] = visited[x][y][dir] + 1
                start.append((nx1, ny1, 7))
        if 0 <= nx2 < N and 0 <= ny2 < M:
            if matrix[nx2][ny2] == '.' and visited[nx2][ny2][6] == -1:
                visited[nx2][ny2][6] = visited[x][y][dir] + 1
                start.append((nx2, ny2, 6))
        if 0 <= nx3 < N and 0 <= ny3 < M:
            if matrix[nx3][ny3] == '.' and visited[nx3][ny3][0] == -1:
                visited[nx3][ny3][0] = visited[x][y][dir] + 1
                start.append((nx3, ny3, 0))