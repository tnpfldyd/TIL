from collections import deque
import sys
input = sys.stdin.readline
while True:
    M, N = map(int, input().split())
    if not M and not N:
        break
    cnt = 1
    cnt2 = 0
    matrix = [list(input().strip()) for _ in range(N)]
    sx, sy = 0, 0
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 'o':
                sx, sy = i, j
                matrix[i][j] = '.'
            elif matrix[i][j] == '*':
                matrix[i][j] = cnt
                cnt *= 2
                cnt2 += 1
    cnt //= 2
    if cnt2 == 0:
        print(0)
        continue
    temp = bin(cnt)[2:]
    keyset = set()
    for i in range(N):
        for j in range(M):
            if isinstance(matrix[i][j], int):
                matrix[i][j] = bin(matrix[i][j])[2:]
                while len(matrix[i][j]) < len(temp):
                    matrix[i][j] = '0' + matrix[i][j]
                keyset.add(matrix[i][j])
    visited = [[[-1] * (2**cnt2) for _ in range(M)] for _ in range(N)]
    visited[sx][sy][0] = 0
    dx, dy = [0,0,-1,1], [-1,1,0,0]
    start = deque()
    start.append((sx, sy, bin(cnt*2)[3:]))
    while start:
        x, y, key = start.popleft()
        if '0' not in key:
            print(visited[x][y][int(key, 2)])
            break
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if matrix[nx][ny] == '.' and visited[nx][ny][int(key, 2)] == -1:
                    visited[nx][ny][int(key, 2)] = visited[x][y][int(key, 2)] + 1
                    start.append((nx, ny, key))
                elif matrix[nx][ny] in keyset:
                    new_key = ''
                    for j in range(cnt2):
                        if key[j] == '1' or matrix[nx][ny][j] == '1':
                            new_key += '1'
                        else:
                            new_key += '0'
                    if visited[nx][ny][int(new_key, 2)] == -1:
                        visited[nx][ny][int(new_key, 2)] = visited[x][y][int(key, 2)] + 1
                        start.append((nx, ny, new_key))
    else:
        print(-1)