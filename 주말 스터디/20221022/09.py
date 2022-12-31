from collections import deque
import sys

input = sys.stdin.readline
N, M = map(int, input().split())
matrix = [list(map(int, input().strip().split())) for _ in range(N)]
answer = [[(0, 0)] * M for _ in range(N)]
result = 0
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
an = 0
visited = [[False] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if matrix[i][j] == 1 and not visited[i][j]:
            start = deque()
            temp = set()
            temp.add((i, j))
            start.append((i, j))
            visited[i][j] = True
            cnt = 1
            while start:
                x, y = start.popleft()
                for k in range(4):
                    nx, ny = x + dx[k], y + dy[k]
                    if 0 <= nx < N and 0 <= ny < M:
                        if matrix[nx][ny] == 1 and not visited[nx][ny]:
                            visited[nx][ny] = True
                            cnt += 1
                            start.append((nx, ny))
                            temp.add((nx, ny))
            for k, v in temp:
                answer[k][v] = (cnt, an)
            an += 1
for i in range(N):
    for j in range(M):
        if matrix[i][j] == 0:
            cnt = 1
            temp = set()
            for k in range(4):
                nx, ny = i + dx[k], j + dy[k]
                if 0 <= nx < N and 0 <= ny < M:
                    temp.add(answer[nx][ny])
            for k in temp:
                cnt += k[0]
            result = max(cnt, result)
print(result)
