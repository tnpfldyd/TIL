from collections import deque
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
matrix = [list(input().rstrip()) for _ in range(N)]
coin = []
for i in range(N):
    for j in range(M):
        if matrix[i][j] == 'o':
            coin.append(i); coin.append(j)
dx, dy = [0,0,1,-1], [1,-1,0,0]
ox, oy, tx, ty = coin
start = deque()
temp = set()
start.append((ox, oy, tx, ty, 0))
temp.add((ox, oy, tx, ty, 0))
answer = False
while start:
    ox, oy, tx, ty, cnt = start.popleft()
    if answer:
        break
    for i in range(4):
        nox, noy, ntx, nty = ox+dx[i], oy+dy[i], tx+dx[i], ty+dy[i]
        if 0 <= nox < N and 0 <= noy < M and 0 <= ntx < N and 0 <= nty < M:
            if matrix[nox][noy] == '#':
                nox, noy = ox, oy
            if matrix[ntx][nty] == '#':
                ntx, nty = tx, ty
            if (nox, noy, ntx, nty, cnt+1) not in temp and cnt < 10:
                start.append((nox, noy, ntx, nty, cnt+1))
                temp.add((nox, noy, ntx, nty, cnt+1))
        elif 0 <= nox < N and 0 <= noy < M and cnt < 10:
            print(cnt+1)
            answer = True
            start.append((nox, noy, ntx, nty, cnt+1))
            break
        elif 0 <= ntx < N and 0 <= nty < M and cnt < 10:
            print(cnt+1)
            answer = True
            start.append((nox, noy, ntx, nty, cnt+1))
            break
else:
    print(-1)