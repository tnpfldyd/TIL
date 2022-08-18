from pprint import pprint
import sys
input = sys.stdin.readline
N = int(input())
matrix = [list(map(int, input().rstrip())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]
result = []
dx, dy = [0, 1, 0, -1],[1, 0, -1, 0]
for x in range(N):
    for y in range(N):
        if matrix[x][y] == 1 and not visited[x][y]:
            start = [(x, y)]
            cnt = 1
            visited[x][y] = True
            while start:
                a, b = start.pop()
                for j in range(4):
                    nx = a + dx[j]; ny = b + dy[j]
                    if 0 <= nx < N and 0 <= ny < N:
                        if matrix[nx][ny] == 1 and not visited[nx][ny]:
                            visited[nx][ny] = True
                            start.append((nx, ny))
                            cnt += 1
            result.append(cnt)
result.sort()
print(len(result))
print(*result, sep = '\n')