from collections import deque
import sys
input = sys.stdin.readline
N, M, K = map(int, input().split())
matrix = [[0] * M for _ in range(N)]
for i in range(K):
    a, b, c, d = map(int, input().split())
    for x in range(b, d):
        for y in range(a, c):
            matrix[x][y] = 1
visited = [[False] * M for _ in range(N)]
result = []
dx, dy = [0,0,1,-1],[1,-1,0,0]
for x in range(N):
    for y in range(M):
        if matrix[x][y] == 0 and not visited[x][y]:
            visited[x][y] = True
            start = deque()
            cnt = 1
            start.append((x, y))
            while start:
                a, b = start.popleft()
                for k in range(4):
                    nx = a + dx[k]; ny = b + dy[k]
                    if 0 <= nx < N and 0 <= ny < M:
                        if matrix[nx][ny] == 0 and not visited[nx][ny]:
                            visited[nx][ny] = True
                            cnt += 1
                            start.append((nx, ny))
            result.append(cnt)
print(len(result))
result.sort()
print(*result)