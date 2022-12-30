from collections import deque
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
matrix = [list(input().strip()) for _ in range(N)]
sx, sy = map(int, input().split())
ex, ey = map(int, input().split())
sx -= 1; sy -= 1; ex -= 1; ey -= 1
def bfs(x, y):
    start = deque()
    start.append((x, y))
    visited = [[0] * M for _ in range(N)]
    visited[x][y] = 1
    dx, dy = [0,0,1,-1], [1,-1,0,0]
    while start:
        x, y = start.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if nx == ex and ny == ey:
                    visited[nx][ny] += 1
                    if matrix[nx][ny] == 'X':
                        return True
                    elif visited[nx][ny] == 2:
                        return True
                    start.append((nx, ny))
                else:
                    if not visited[nx][ny] and matrix[nx][ny] == '.':
                        visited[nx][ny] = 1
                        start.append((nx, ny))
    return False
answer = bfs(sx, sy)
print('YES' if answer else 'NO')