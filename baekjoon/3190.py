from collections import deque
import sys
input = sys.stdin.readline
N = int(input())
matrix = [[0] * N for _ in range(N)]
for i in range(int(input())):
    a, b = map(int, input().split())
    matrix[a-1][b-1] = 'a'
command = deque()
for i in range(int(input())):
    a, b = input().rstrip().split()
    a = int(a)
    command.append((a, b))
x, y = 0, 0
cnt = 0
dx, dy = [0,1,0,-1],[1,0,-1,0]
start = 0
if len(command) > 0:
    if command[0][0] == cnt:
        num, asdw = command.popleft()
        if asdw == 'D':
            start = (start + 1) % 4
        else:
            start = (start + 3) % 4
temp = deque()
temp.append((x, y))
matrix[x][y] = 1
while True:
    cnt += 1
    x += dx[start]; y += dy[start]
    if 0 <= x < N and 0 <= y < N:
        if matrix[x][y] == 'a':
            matrix[x][y] = 1
            temp.append((x, y))
            if len(command) > 0:
                if command[0][0] == cnt:
                    num, asdw = command.popleft()
                    if asdw == 'D':
                        start = (start + 1) % 4
                    else:
                        start = (start + 3) % 4
        elif matrix[x][y] == 0:
            matrix[x][y] = 1
            temp.append((x, y))
            tx, ty = temp.popleft()
            matrix[tx][ty] = 0
            if len(command) > 0:
                if command[0][0] == cnt:
                    num, asdw = command.popleft()
                    if asdw == 'D':
                        start = (start + 1) % 4
                    else:
                        start = (start + 3) % 4
        else:
            break
    else:
        break
print(cnt)
