from collections import deque
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
matrix = [list(input().strip()) for _ in range(N)]
rx, ry, bx, by, ex, ey  = 0, 0, 0, 0, 0, 0
for i in range(N):
    for j in range(M):
        if matrix[i][j] == 'R':
            rx, ry = i, j
        elif matrix[i][j] == 'B':
            bx, by = i, j
        elif matrix[i][j] == 'O':
            ex, ey = i, j
dx, dy = [0,0,1,-1], [1,-1,0,0]
direction = {0 : 'R', 1 : 'L', 2 : 'D', 3 : 'U'}
start = deque()
start.append((rx, ry, bx, by, 0, ''))
temp = set()
answer = False
while start:
    rx, ry, bx, by, cnt, dir = start.popleft()
    if cnt == 10:
        print(-1)
        answer = True
        break
    if answer:
        break
    for i in range(4):
        nrx, nry, nbx, nby = rx, ry, bx, by
        while True:
            nrx += dx[i]; nry += dy[i]
            if matrix[nrx][nry] == '#':
                nrx -= dx[i]; nry -= dy[i]
                break
            elif nrx == ex and nry == ey:
                break
        while True:
            nbx += dx[i]; nby += dy[i]
            if matrix[nbx][nby] == '#':
                nbx -= dx[i]; nby -= dy[i]
                break
            elif nbx == ex and nby == ey:
                break
        if nbx == ex and nby == ey:
            continue
        if nrx == ex and nry == ey:
            print(cnt + 1)
            print(dir + direction[i])
            answer = True
            break
        if nrx == nbx and nry == nby:
            if abs(nrx - rx) + abs(nry - ry) > abs(nbx - bx) + abs(nby - by):
                nrx -= dx[i]; nry -= dy[i]
            else:
                nbx -= dx[i]; nby -= dy[i]
        if (nrx, nry, nbx, nby) not in temp:
            temp.add((nrx, nry, nbx, nby))
            start.append((nrx, nry, nbx, nby, cnt + 1, dir + direction[i]))
if not answer:
    print(-1)