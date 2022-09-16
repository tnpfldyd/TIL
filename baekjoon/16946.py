from collections import deque
import sys
input = sys.stdin.readline
zerodic = {}
N, M = map(int, input().split())
matrix = [list(input().rstrip()) for _ in range(N)]
dx, dy = [0,0,1,-1], [1,-1,0,0]
zerovisited = [[False] * M for _ in range(N)]
zerocnt = 2
new_matrix = [[0] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if matrix[i][j] == '0':
            zerovisited[i][j] = True
            cnt = 1
            matrix[i][j] = zerocnt
            start = deque()
            start.append((i, j))
            while start:
                x, y = start.popleft()
                for k in range(4):
                    nx, ny = x + dx[k], y + dy[k]
                    if 0 <= nx < N and 0 <= ny < M:
                        if matrix[nx][ny] == '0' and not zerovisited[nx][ny]:
                            zerovisited[nx][ny] = True
                            matrix[nx][ny] = zerocnt
                            cnt += 1
                            start.append((nx, ny))
            zerodic[zerocnt] = cnt
            zerocnt += 1
for i in range(N):
    for j in range(M):
        if matrix[i][j] == '1':
            cnt = 1
            k2 = set()
            for k in range(4):
                nx, ny = i + dx[k], j + dy[k]
                if 0 <= nx < N and 0 <= ny < M:
                    if matrix[nx][ny] != '1':
                        k2.add(matrix[nx][ny])
            for k in k2:
                cnt += zerodic.get(k)
            new_matrix[i][j] = cnt
for i in new_matrix:
    for j in i:
        print(j%10, end='')
    print()