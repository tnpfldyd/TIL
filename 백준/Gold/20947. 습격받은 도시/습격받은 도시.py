import sys
input = sys.stdin.readline

N = int(input())
matrix = [list(input().strip()) for _ in range(N)]

dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]

def isVaild(x, y):
    return 0 <= x < N and 0 <= y < N

for x in range(N):
    for y in range(N):
        if matrix[x][y] == 'X':
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                while isVaild(nx, ny) and matrix[nx][ny] == '.':
                    matrix[nx][ny] = 'B'
                    nx, ny = nx + dx[i], ny + dy[i]

for x in range(N):
    for y in range(N):
        if matrix[x][y] == 'O':
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                while isVaild(nx, ny) and (matrix[nx][ny] == 'B' or matrix[nx][ny] == '.'):
                    matrix[nx][ny] = '.'
                    nx, ny = nx + dx[i], ny + dy[i]
for arr in matrix:
    print(''.join(arr))