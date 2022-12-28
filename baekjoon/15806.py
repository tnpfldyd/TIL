from collections import deque
import sys
input = sys.stdin.readline
N, M, K, t = map(int, input().split())
visited = [[[False] * N for _ in range(N)] for _ in range(2)]
start = deque()
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1; b -= 1
    visited[0][a][b] = True
    start.append((a, b, 0))

dx, dy = [1,1,-1,-1,2,2,-2,-2],[2,-2,2,-2,1,-1,1,-1]
while start:
    x, y, time = start.popleft()
    breeding = False
    for i in range(8):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < N and not visited[(time+1)%2][nx][ny]:
            visited[(time+1)%2][nx][ny] = True
            if time+1 < t:
                start.append((nx, ny, time+1))
            breeding = True
    if not breeding:
        visited[(time)%2][x][y] = False
answer = False
for _ in range(K):
    a, b = map(int, input().split())
    a -= 1; b -= 1
    if visited[t%2][a][b]:
        answer = True
print('YES' if answer else 'NO')