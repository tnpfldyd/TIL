from pprint import pprint
import sys
sys.stdin = open('13567input.txt', 'r')
M, n = map(int, input().split())
M += 1
matrix = [[0] * M for _ in range(M)]
dx, dy = [0, 1, 0, -1],[1, 0, -1, 0] # 우 하 좌 상
x, y = 0, 0
start = 0
for i in range(n):
    command, times = input().split()
    if command == 'TURN':
        if times == '0':
            if start + 1 == 4:
                start = 0
            else:
                start += 1
        else:
            if start - 1 < 0:
                start = 3
            else:
                start -= 1
    else:
        if 0 <= x + (int(times) * dx[start]) < M and 0 <= y + (int(times) * dy[start])< M:
            matrix[x][y] = 0
            x += int(times) * dx[start]; y += int(times) * dy[start]
            matrix[x][y] = 1
        else:
            print(-1)
            break
else:
    print(y, x)
