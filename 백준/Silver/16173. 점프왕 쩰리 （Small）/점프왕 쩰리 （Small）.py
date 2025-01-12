from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
sx, sy = 0, 0        
visited = [[False] * N for _ in range(N)]
visited[sx][sy] = True
q = deque()
q.append((sx, sy))
dx, dy = [0, 1], [1, 0]
result = 0
while q:
    x, y = q.popleft()
    if (x, y) == (N - 1, N - 1):
        print("HaruHaru")
        break
    for i in range(2):
        nx, ny = x + dx[i] * matrix[x][y], y + dy[i] * matrix[x][y]
        if 0 <= nx < N and 0 <= ny < N:
            if not visited[nx][ny] and matrix[nx][ny] != 'X':
                visited[nx][ny] = True
                q.append((nx, ny))
                if matrix[nx][ny] == 'P':
                    result += 1
else:
    print("Hing")