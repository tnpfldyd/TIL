from collections import deque
import sys
input = sys.stdin.readline
dx, dy = [0,0,1,-1], [1,-1,0,0]
N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
cnt = 0
last = 0
while True:
    start = deque()
    temp = set()
    visited = [[False] * M for _ in range(N)]
    visited[0][0] = True
    start.append((0, 0))
    while start:
        x, y = start.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if not visited[nx][ny]:
                    if matrix[nx][ny] == 1:
                        visited[nx][ny] = True
                        temp.add((nx, ny))
                    else:
                        visited[nx][ny] = True
                        start.append((nx, ny))
    if len(temp) == 0:
        break
    else:
        last = len(temp)
        for k, v in temp:
            matrix[k][v] = 0
        cnt += 1
print(cnt)
print(last)
    