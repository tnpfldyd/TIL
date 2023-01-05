from collections import deque
import sys
input = sys.stdin.readline
INF = sys.maxsize
N = int(input())
matrix = [list(input().strip()) for _ in range(N)]
altitude = [list(map(int, input().strip().split())) for _ in range(N)]
house, alti_set = 0, set()
sx, sy = 0, 0
dx, dy = [0,0,-1,1,1,1,-1,-1], [-1,1,0,0,1,-1,1,-1]
for i in range(N):
    for j in range(N):
        alti_set.add(altitude[i][j])
        if matrix[i][j] == 'P':
            sx, sy = i, j
        elif matrix[i][j] == 'K':
            house += 1
alti_set = sorted(alti_set)
answer = INF
left, right = 0, 0

while left < len(alti_set):
    cnt = 0
    if alti_set[left] <= altitude[sx][sy] <= alti_set[right]:
        start = deque()
        start.append((sx, sy))
        visited = [[False] * N for _ in range(N)]
        visited[sx][sy] = True
        while start:
            x, y = start.popleft()
            if matrix[x][y] == 'K':
                cnt += 1
            for i in range(8):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                    if alti_set[left] <= altitude[nx][ny] <= alti_set[right]:
                        visited[nx][ny] = True
                        start.append((nx, ny))
    if cnt == house:
        if answer > alti_set[right] - alti_set[left]:
            answer = alti_set[right] - alti_set[left]
        left += 1
    elif right + 1 < len(alti_set):
        right += 1
    else:
        break
print(answer)