import sys
input = sys.stdin.readline

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

def check(x, y, cur):
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N:
            if map[nx][ny] == '#' and cur > 0:
                cur -= 1
                map[nx][ny] = '*'
            elif map[nx][ny] == '*' and cur > 0:
                cur -= 1
            elif map[nx][ny] == '#' and cur == 0:
                map[nx][ny] = '-'

N = int(input().strip())
map = [list(input().strip()) for _ in range(N)]
cnt = 0

for i in range(N):
    for j in range(N):
        if map[i][j].isdigit():
            cur = int(map[i][j])
            check(i, j, cur)

for i in range(N):
    for j in range(N):
        if map[i][j] in ('*', '#'):
            cnt += 1

print(cnt)