from collections import deque
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
matrix = [list(map(int, input().strip())) for _ in range(N)]
cnt = 0
dx, dy = [0,0,1,-1], [1,-1,0,0]
for i in range(1, 10):
    visited = [[False] * M for _ in range(N)]
    for x in range(N):
        for y in range(M):
            if matrix[x][y] and matrix[x][y] < i and not visited[x][y]:
                start = deque()
                water = set()
                water.add((x, y))
                start.append((x, y))
                visited[x][y] = True
                answer = False
                while start:
                    k, v = start.popleft()
                    for j in range(4):
                        nx, ny = k + dx[j], v + dy[j]
                        if 0 <= nx < N and 0 <= ny < M and matrix[nx][ny]:
                            if not visited[nx][ny] and matrix[nx][ny] < i:
                                visited[nx][ny] = True
                                water.add((nx, ny))
                                start.append((nx, ny))
                        else:
                            answer = True
                if not answer:
                    for k, v in water:
                        matrix[k][v] += 1
                        cnt += 1
print(cnt)