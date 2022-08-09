T = int(input())
for i in range(1, T+1):
    N = int(input())
    dx, dy = [0, 1, 0, -1],[1, 0, -1, 0]
    matrix = [[0] * N for _ in range(N)]
    start = [(0, 0)]
    s, f = 1, 0
    matrix[0][0] = 1
    while start:
        x, y = start.pop(0)
        if s == N*N:
            break
        if 0 <= x + dx[f] < N and 0 <= y + dy[f] < N and matrix[x + dx[f]][y + dy[f]] == 0:
            s += 1
            nx, ny = x + dx[f] , y + dy[f]
            matrix[nx][ny] = s
            start.append((nx, ny))
        else:
            f = (f + 1) % 4
            start.append((x, y))
    print(f'#{i}')
    for j in matrix:
        print(*j)