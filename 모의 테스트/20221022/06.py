from collections import deque

N = int(input())
matrix = [[0] * N for _ in range(N)]

r, c = [-2, -2, 0, 0, 2, 2], [-1, 1, -2, 2, -1, 1]
a, b, q, w = map(int, input().split())
matrix[a][b] = 1
start = deque()
start.append((a, b))
while start:
    x, y = start.popleft()
    if x == q and y == w:
        print(matrix[q][w] - 1)
        break
    for i in range(6):
        nx, ny = x + r[i], y + c[i]
        if 0 <= nx < N and 0 <= ny < N:
            if matrix[nx][ny] == 0:
                matrix[nx][ny] = matrix[x][y] + 1
                start.append((nx, ny))
else:
    print(-1)
