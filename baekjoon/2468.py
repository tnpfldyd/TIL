from pprint import pprint
import sys
input = sys.stdin.readline
T = int(input())
matrix = [list(map(int, input().rstrip().split())) for _ in range(T)]
high = max(map(max, matrix))
result = []
dx, dy = [0, 1, 0, -1], [-1, 0, 1, 0]
for i in range(high+1):
    visited = [[False] * T for _ in range(T)]
    for x in range(T):
        for y in range(T):
            if matrix[x][y] <= i and not visited[x][y]:
                visited[x][y] = True
                start = [(x, y)]
                while start:
                    a, b = start.pop()
                    for j in range(4):
                        nx = x + dx[j]; ny = y + dy[j]
                        if 0 <= nx < T and 0 <= ny < T:
                            if matrix[nx][ny] <= i and not visited[nx][ny]:
                                visited[nx][ny] = True
                                start.append((nx, ny))
    cnt = 0
    visit = [[0] * T for _ in range(T)]
    for x in range(T):
        for y in range(T):
            if not visited[x][y] and visit[x][y] == 0:
                vi_start = [(x, y)]
                cnt += 1
                visit[x][y] = 1
                while vi_start:
                    tx, ty = vi_start.pop()
                    for j in range(4):
                        vx = tx + dx[j]; vy = ty + dy[j]
                        if 0 <= vx < T and 0 <= vy < T:
                            if not visited[vx][vy] and visit[vx][vy] == 0:
                                visit[vx][vy] = 1
                                vi_start.append((vx, vy))
    result.append(cnt)
print(max(result))