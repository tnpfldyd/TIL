from collections import deque
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
light_dic = {}
for _ in range(M):
    a, b, c, d = map(int, input().split())
    a -= 1; b -= 1; c -= 1; d -= 1
    if (a, b) not in light_dic:
        light_dic[(a, b)] = [(c, d)]
    else:
        light_dic[(a, b)].append((c, d))
visited = [[0] * N for _ in range(N)]
light = [[0] * N for _ in range(N)]
possible = [[0] * N for _ in range(N)]
light[0][0] = 1
visited[0][0] = 1
possible[0][0] = 1
cnt = 1
start = deque()
start.append((0, 0))
dx, dy = [0,0,1,-1], [1,-1,0,0]
while start:
    x, y = start.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < N:
            if not possible[nx][ny]:
                possible[nx][ny] = 1
    if light_dic.get((x, y)) != None:
        for nx, ny in light_dic[(x, y)]:
            if not light[nx][ny]:
                light[nx][ny] = 1
                cnt += 1
    for i in range(N):
        for j in range(N):
            if possible[i][j] and light[i][j] and not visited[i][j]:
                visited[i][j] = 1
                start.append((i, j))
print(cnt)