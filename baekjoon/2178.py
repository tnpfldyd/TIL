N, M = map(int, input().split())
matrix = [list(map(int, input())) for _ in range(N)]
low = [1,0,-1]
col = [0,1,0]
for x in range(N):
    for y in range(M):
        if matrix[x][y] != 0:
            for k in range(3):
                nx = x + low[k]
                ny = y = col[k]
                cnt = 1
                while 0 <= nx < M and 0 <= ny < N and matrix[nx][ny] == matrix[x][y]:
                    cnt += 1
                    nx += low[k]
                    ny += col[k]
                if 0 <= nx < M and 0 <= ny < N and matrix[nx][ny] != matrix[x][y]:
                    for j in range(3):
                        jx = nx + low[k]
                        jy = ny + col[y]
                        while 0 <= jx < M and 0 <= jy < N and matrix[jx][jy] == matrix[x][y]:
                            cnt += 1
                            jx += low[k]
                            jy += col[y]
                            