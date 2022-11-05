from collections import deque
import sys
input = sys.stdin.readline
while True:
    M, N = map(int, input().split())
    if M == 0 and N == 0:
        break
    matrix1 = []
    matrix2 = []
    for _ in range(N):
        a, b = input().split()
        matrix1.append(list(a)); matrix2.append(list(b))
    sx1, sy1, ex1, ey1, sx2, sy2, ex2, ey2 = 0,0,0,0,0,0,0,0
    dx, dy = [1,-1,0,0], [0,0,1,-1]
    for i in range(N):
        for j in range(M):
            if matrix1[i][j] == '%':
                ex1, ey1 = i, j
            elif matrix1[i][j] == 'L':
                sx1, sy1 = i, j
            if matrix2[i][j] == '%':
                ex2, ey2 = i, j
            elif matrix2[i][j] == 'R':
                sx2, sy2 = i, j
    start = deque()
    visited = set()
    visited.add((sx1, sy1, sx2, sy2))
    start.append((sx1, sy1, sx2, sy2))
    
    while start:
        lx, ly, rx, ry = start.popleft()
        if lx == ex1 and ly == ey1 and rx == ex2 and ry == ey2:
            print('Yes')
            break

        for k in range(2):
            nlx, nly, nrx, nry = lx + dx[k], ly + dy[k], rx + dx[k], ry + dy[k]
            if 0 <= nlx < N and 0 <= nly < M and 0 <= nrx < N and 0 <= nry < M:
                if matrix1[nlx][nly] == '#':
                    nlx, nly = lx, ly
                if matrix2[nrx][nry] == '#':
                    nrx, nry = rx, ry
                if (nlx, nly, nrx, nry) not in visited:
                    visited.add((nlx, nly, nrx, nry))
                    start.append((nlx, nly, nrx, nry))
        nlx, nly, nrx, nry = lx + dx[2], ly + dy[2], rx + dx[3], ry + dy[3]
        if 0 <= nlx < N and 0 <= nly < M and 0 <= nrx < N and 0 <= nry < M:
            if matrix1[nlx][nly] == '#':
                nlx, nly = lx, ly
            if matrix2[nrx][nry] == '#':
                nrx, nry = rx, ry
            if (nlx, nly, nrx, nry) not in visited:
                visited.add((nlx, nly, nrx, nry))
                start.append((nlx, nly, nrx, nry))
        nlx, nly, nrx, nry = lx + dx[3], ly + dy[3], rx + dx[2], ry + dy[2]
        if 0 <= nlx < N and 0 <= nly < M and 0 <= nrx < N and 0 <= nry < M:
            if matrix1[nlx][nly] == '#':
                nlx, nly = lx, ly
            if matrix2[nrx][nry] == '#':
                nrx, nry = rx, ry
            if (nlx, nly, nrx, nry) not in visited:
                visited.add((nlx, nly, nrx, nry))
                start.append((nlx, nly, nrx, nry))
    else:
        print('No')