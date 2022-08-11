from pprint import pprint
import sys
sys.stdin = open('test.txt', 'r')

N, M = map(int, input().split())
matrix = [input().split() for _ in range(N)]
visited = [[0] * M for _ in range(N)]
dx, dy = [0, 1, 0, -1],[1, 0, -1, 0] # 우 하 좌 상
for x in range(N):
    for y in range(M):
        if matrix[x][y] == '0' and visited[x][y] == 0:
            start = [(0, 0)]
            visited[x][y] = 1
            while start:
                a, b = start.pop()
                for i in range(4):
                    nx = a + dx[i]
                    ny = b + dy[i]
                    if 0 <= nx < N and 0 <= ny < M:
                        if matrix[nx][ny] == '0' and visited[nx][ny] == 0:
                            visited[nx][ny] = visited[a][b] + 1
                            start.append((nx, ny))                          
                            if nx == N-1 and ny == M -1:
                                break
start2 = [(N-1, M -1)]
result = []
result.append((N-1, M -1))
while start2:
    x, y = start2.pop()
    if x == 0 and y == 0:
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if visited[x][y] -1 == visited[nx][ny]:
                result.append((nx, ny))
                start2.append((nx, ny))
print(result[::-1])