from collections import deque
import sys
input = sys.stdin.readline
N = int(input())
matrix = []
sx, sy = 0, 0
for i in range(N):
    temp = list(map(int, input().strip().split()))
    matrix.append(temp)
    for j in range(N):
        if temp[j] == 1:
            sx, sy = i, j
nx, ny = [1,2,1,2,-1,-2,-1,-2], [-2,-1,2,1,2,1,-2,-1]
bx, by = [1,1,-1,-1], [1,-1,1,-1]
lx, ly = [0,0,1,-1], [1,-1,0,0]
visited = [[[[-1] * (N*N+1) for _ in range(N)] for _ in range(N)] for _ in range(3)]
start = deque()
for i in range(3):
    start.append((i, 1, sx, sy))
    visited[i][sx][sy][1] = 0
while start:
    piecetype, target, x, y = start.popleft()
    if target == N*N:
        print(visited[piecetype][x][y][target])
        break
    elif not piecetype:
        for i in range(8):
            dx, dy = x + nx[i], y + ny[i]
            if 0 <= dx < N and 0 <= dy < N:
                if matrix[dx][dy] == target + 1 and visited[piecetype][dx][dy][target+1] == -1:
                    visited[piecetype][dx][dy][target+1] = visited[piecetype][x][y][target] + 1
                    start.append((piecetype, target+1, dx, dy))
                    
                if visited[piecetype][dx][dy][target] == -1:
                    visited[piecetype][dx][dy][target] = visited[piecetype][x][y][target] + 1
                    start.append((piecetype, target, dx, dy))
    elif piecetype == 1:
        for i in range(4):
            dx, dy = x, y
            while 0 <= dx + bx[i] < N and 0 <= dy + by[i] < N:
                dx += bx[i]; dy += by[i]
                if matrix[dx][dy] == target + 1 and visited[piecetype][dx][dy][target+1] == -1:
                    visited[piecetype][dx][dy][target+1] = visited[piecetype][x][y][target] + 1
                    start.append((piecetype, target+1, dx, dy))
                if visited[piecetype][dx][dy][target] == -1:
                    visited[piecetype][dx][dy][target] = visited[piecetype][x][y][target] + 1
                    start.append((piecetype, target, dx, dy))
    else:
        for i in range(4):
            dx, dy = x, y
            while 0 <= dx + lx[i] < N and 0 <= dy + ly[i] < N:
                dx += lx[i]; dy += ly[i]
                if matrix[dx][dy] == target + 1 and visited[piecetype][dx][dy][target+1] == -1:
                    visited[piecetype][dx][dy][target+1] = visited[piecetype][x][y][target] + 1
                    start.append((piecetype, target+1, dx, dy))
                if visited[piecetype][dx][dy][target] == -1:
                    visited[piecetype][dx][dy][target] = visited[piecetype][x][y][target] + 1
                    start.append((piecetype, target, dx, dy))
    for i in range(3):
        if i == piecetype:
            continue
        if visited[i][x][y][target] == -1:
            visited[i][x][y][target] = visited[piecetype][x][y][target] + 1
            start.append((i, target, x, y))