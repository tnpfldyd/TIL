from collections import deque
import sys
input = sys.stdin.readline
while True:
    L, R, C = map(int, input().split())
    if (L, R, C) == (0, 0, 0):
        break
    matrix = []
    start = ''
    end = ''

    for i in range(L):
        board = []
        for j in range(R):
            row = list(input().strip())
            for k in range(C):
                if row[k] == 'S':
                    start = (i, j, k)
                elif row[k] == 'E':
                    end = (i, j, k)
            board.append(row)
        input()
        matrix.append(board)

    q = deque()
    sf, sx, sy = start
    visited = [[[False] * C for _ in range(R)] for _ in range(L)]
    visited[sf][sx][sy] = True
    q.append((sf, sx, sy, 0))
    dx, dy, df = (1, -1, 0, 0, 0, 0), (0, 0, 1, -1, 0, 0), (0, 0, 0, 0, 1, -1)

    while q:
        f, x, y, cnt = q.popleft()
        if (f, x, y) == end:
            print(f'Escaped in {cnt} minute(s).')
            break
        for i in range(6):
            nf, nx, ny = f + df[i], x + dx[i], y + dy[i]
            if 0 <= nf < L and 0 <= nx < R and 0 <= ny < C:
                if matrix[nf][nx][ny] == '#':
                    continue

                if not visited[nf][nx][ny]:
                    visited[nf][nx][ny] = True
                    q.append((nf, nx, ny, cnt + 1))
    else:
        print('Trapped!')