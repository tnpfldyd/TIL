from collections import deque
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
visited = [[False] * M for _ in range(N)]
matrix = [list(input().rstrip()) for _ in range(N)]
dx, dy = [0,0,-1,1],[1,-1,0,0]
wolf_final = []
sheep_final = []
for x in range(N):
    for y in range(M):
        if matrix[x][y] == '.' or matrix[x][y] == 'v' or matrix[x][y] == 'o':
            if not visited[x][y]:
                visited[x][y] = True
                wolf = 0
                sheep = 0
                if matrix[x][y] == 'v':
                    wolf += 1
                elif matrix[x][y] == 'o':
                    sheep += 1
                start = deque()
                start.append((x, y))
                while start:
                    a, b = start.popleft()
                    for i in range(4):
                        nx, ny = a + dx[i], b + dy[i]
                        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and matrix[nx][ny] != '#':
                            if matrix[nx][ny] == 'v':
                                wolf += 1
                            elif matrix[nx][ny] == 'o':
                                sheep += 1
                            visited[nx][ny] = True
                            start.append((nx, ny))
                if wolf >= sheep:
                    wolf_final.append(wolf)
                else:
                    sheep_final.append(sheep)
print(sum(sheep_final), sum(wolf_final))