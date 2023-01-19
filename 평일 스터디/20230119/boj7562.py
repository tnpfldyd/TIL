from collections import deque
import sys
input = sys.stdin.readline
dx, dy = [-2,-1,1,2,2,1,-1,-2],[-1,-2,-2,-1,1,2,2,1]
T = int(input())
for i in range(T):
    N = int(input())
    matrix = [[-1] * N for _ in range(N)]
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    start = deque()
    start.append((a, b))
    matrix[a][b] = 0
    while start:
        x, y = start.popleft()
        if x == c and y == d:
            print(matrix[x][y])
            break
        for j in range(8):
            nx = x + dx[j]; ny = y + dy[j]
            if 0 <= nx < N and 0 <= ny < N:
                if matrix[nx][ny] == -1:
                    matrix[nx][ny] = matrix[x][y] + 1
                    start.append((nx, ny))