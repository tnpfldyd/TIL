from collections import deque
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
matrix = [list(map(int, input().strip().split())) for _ in range(N)]
onestart = deque()
twostart = deque()
for i in range(N):
    for j in range(M):
        if matrix[i][j] == 1:
            onestart.append((i, j))
        elif matrix[i][j] == 2:
            twostart.append((i, j))
dx, dy = [0,0,1,-1], [1,-1,0,0]
while onestart or twostart:
    temp = {}
    onetemp = set()
    twotemp = set()
    for i in range(len(onestart)):
        x, y = onestart.popleft()
        for j in range(4):
            nx, ny = x + dx[j], y + dy[j]
            if 0 <= nx < N and 0 <= ny < M:
                if matrix[nx][ny] == 0:
                    onetemp.add((nx, ny))
    for i in range(len(twostart)):
        x, y = twostart.popleft()
        for j in range(4):
            nx, ny = x + dx[j], y + dy[j]
            if 0 <= nx < N and 0 <= ny < M:
                if matrix[nx][ny] == 0:
                    twotemp.add((nx, ny))
    for a, b in onetemp:
        if (a, b) not in temp:
            temp[(a, b)] = 'a'
        else:
            temp[(a, b)] += 'a'
    for a, b in twotemp:
        if (a, b) not in temp:
            temp[(a, b)] = 'b'
        else:
            temp[(a, b)] += 'b'
    for k, v in temp.items():
        if v == 'a':
            onestart.append(k)
            matrix[k[0]][k[1]] = 1
        elif v == 'b':
            twostart.append(k)
            matrix[k[0]][k[1]] = 2
        else:
            matrix[k[0]][k[1]] = 3
one, two, three = 0, 0, 0
for i in range(N):
    for j in range(M):
        if matrix[i][j] == 1:
            one += 1
        elif matrix[i][j] == 2:
            two += 1
        elif matrix[i][j] == 3:
            three += 1
print(one, two, three)