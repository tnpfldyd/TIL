from collections import deque
import sys
sys.stdin = open('5427input.txt', 'r')
input = sys.stdin.readline
T = int(input())
for q in range(T):
    r, c = map(int, input().split())
    matrix = [list(input().rstrip()) for _ in range(c)]
    jcnt = [[0] * r for _ in range(c)]
    start = deque()
    dx, dy = [0,0,-1,1],[1,-1,0,0]
    f = False
    for i in range(c):
        for j in range(r):
            if matrix[i][j] == '*':
                start.append((i, j))
    for i in range(c):
        for j in range(r):
            if matrix[i][j] == '@':
                start.append((i, j))
                jcnt[i][j] = 1
                if (i == c-1 or i == 0) or (j == r-1 or j == 0):
                    print(jcnt[i][j])
                    f = True
                    break
                else:
                    break
    while start:
        x, y = start.popleft()
        if f == True:
            break
        for i in range(4):
            nx = x + dx[i]; ny = y + dy[i]
            if 0 <= nx < c and 0 <= ny < r:
                if '@' in matrix[x][y] and '*' not in matrix[nx][ny] and matrix[nx][ny] != '#':
                    if jcnt[nx][ny] == 0:
                        matrix[nx][ny] = '@'
                        jcnt[nx][ny] = jcnt[x][y] + 1
                        if (nx == c-1 or nx == 0) or (ny == r-1 or ny == 0):
                            print(jcnt[nx][ny])
                            f = True
                            break
                        start.append((nx, ny))
                if '*' in matrix[x][y]:
                    if matrix[nx][ny] == '@' or matrix[nx][ny] == '.':
                        matrix[nx][ny] += '*'
                        start.append((nx, ny))
    if f == False:
        print('IMPOSSIBLE')
