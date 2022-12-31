from collections import deque
import sys
sys.stdin = open('swea1226_input.txt')
for i in range(10):
    case = int(input())
    matrix = [list(map(int, input())) for _ in range(16)]
    vistited = [[False] * 16 ]
    start = deque()
    true = False
    for x in range(16):
        for y in range(16):
            if matrix[x][y] == 2:
                true = True
                start.append((x, y))
        if true:
            break
    dx, dy = [0,0,1,-1],[1,-1,0,0]
    while start:
        x, y = start.popleft()
        if matrix[x][y] == 3:
            print(f'#{case} 1')
            break
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < 16 and 0 <= ny < 16:
                if matrix[nx][ny] == 0:
                    matrix[nx][ny] = matrix[x][y] - 100
                    start.append((nx, ny))
                elif matrix[nx][ny] == 3:
                    start.append((nx, ny))
    else:
        print(f'#{case} 0')
