from collections import deque
import sys
# sys.stdin = open('4179input.txt', 'r')
input = sys.stdin.readline

r, c = map(int, input().split())
matrix = [list(input().rstrip()) for _ in range(r)]
jcnt = [[0] * c for _ in range(r)]
start = deque()
dx, dy = [0,0,-1,1],[1,-1,0,0]
Jtemp = deque()

for i in range(r):
    for j in range(c):
        if matrix[i][j] == 'F':
            start.append((i, j))
for i in range(r):
    for j in range(c):
        if matrix[i][j] == 'J':
            start.append((i, j))
            Jtemp.append((i, j))
            jcnt[i][j] = 1
            if (i == r-1 or i == 0) or (j == c-1 or j == 0):
                print(jcnt[i][j])
                sys.exit(0)
            else:
                break
while start:
    x, y = start.popleft()
    for i in range(4):
        nx = x + dx[i]; ny = y + dy[i]
        if 0 <= nx < r and 0 <= ny < c:
            if 'J' in matrix[x][y] and 'F' not in matrix[nx][ny] and matrix[nx][ny] != '#':
                if jcnt[nx][ny] == 0:
                    matrix[nx][ny] = 'J'
                    jcnt[nx][ny] = jcnt[x][y] + 1
                    if (nx == r-1 or nx == 0) or (ny == c-1 or ny == 0):
                        print(jcnt[nx][ny])
                        sys.exit(0)
                    start.append((nx, ny))
            if 'F' in matrix[x][y]:
                if matrix[nx][ny] == 'J' or matrix[nx][ny] == '.':
                    matrix[nx][ny] += 'F'
                    start.append((nx, ny))
else:
    print('IMPOSSIBLE')
