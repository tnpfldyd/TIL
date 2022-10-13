from collections import deque
import sys
input = sys.stdin.readline
matrix = deque([list(input().strip()) for _ in range(8)])
start = deque()
start.append((7, 0))
dx, dy = [0,0,-1,1,0,-1,1,1,-1],[-1,1,0,0,0,1,1,-1,-1]
answer = 0
while start:
    visited = [[False] * 8 for _ in range(8)]
    if answer:
        break
    for _ in range(len(start)):
        x, y = start.popleft()
        if x == 0 and y == 7:
            print(1)
            answer = 1
            break
        if matrix[x][y] == '#':
            continue
        for k in range(9):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < 8 and 0 <= ny < 8:
                if matrix[nx][ny] != '#' and not visited[nx][ny]:
                    visited[nx][ny] = True
                    start.append((nx, ny))
    matrix.pop()
    matrix.appendleft(['.', '.', '.', '.', '.', '.', '.', '.'])
else:
    print(0)