from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
matrix = [list(map(int, input().rstrip().split())) for _ in range(N)]
start = []

for i in range(N):
    for j in range(N):
        if matrix[i][j] != 0:
            start.append((i, j, matrix[i][j]))

start = deque(sorted(start, key = lambda x : x[2]))

dx, dy = [-1,1,0,0],[0,0,1,-1]
S, X, Y = map(int, input().split())
cnt = 0
while start:
    if cnt == S:
        break
    for _ in range(len(start)):
        x, y, num = start.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if not matrix[nx][ny]:
                    matrix[nx][ny] = num
                    start.append((nx, ny, num))
    cnt += 1

print(matrix[X-1][Y-1])