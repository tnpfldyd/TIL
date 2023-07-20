from collections import deque

S, E = map(int, input().split())
sx, sy = 0, 0
dx, dy = [-1, 0, 1, 1, 0, -1], [0, 1, 1, 0, -1, -1]
matrix = [[0] * 1500 for _ in range(1500)]
visited = [[0] * 1500 for _ in range(1500)]

def draw():
    global sx, sy
    x, y, N, K = 750, 750, 1, 1
    matrix[x][y] = 1
    while True:
        for i in range(6):
            for k in range(K - 1 if i == 1 else K):
                nx, ny = x + dx[i], y + dy[i]
                N += 1
                matrix[nx][ny] = N
                if N == S:
                    sx, sy = nx, ny
                if N == 1000000:
                    return
                x, y = nx, ny
        K += 1
draw()

start = deque()
start.append((sx, sy))
visited[sx][sy] = -1
while start:
    x, y = start.popleft()
    if matrix[x][y] == E:
        stack = []
        while True:
            stack.append(matrix[x][y])
            if visited[x][y] == -1:
                break
            for i in range(6):
                nx, ny = x + dx[i], y + dy[i]
                if matrix[nx][ny] == visited[x][y]:
                    x, y = nx, ny
                    break
        print(*stack[::-1])
        break
    for i in range(6):
        nx, ny = x + dx[i], y + dy[i]
        if not matrix[nx][ny] or visited[nx][ny]:
            continue
        visited[nx][ny] = matrix[x][y]
        start.append((nx, ny))
