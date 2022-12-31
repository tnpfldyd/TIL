import sys
input = sys.stdin.readline
N, M = map(int, input().split())
matrix = [list(map(int, input().rstrip().split())) for _ in range(N)]
dx, dy = [0, 1, 0, -1], [-1, 0, 1, 0]
final = 0
while max(map(max, matrix)):
    visit = [[False] * M for _ in range(N)]
    all = 0
    for x in range(N):
        for y in range(M):
            if matrix[x][y] != 0 and not visit[x][y]:
                visit[x][y] = True
                start = [(x, y)]
                all += 1
                while start:
                    a, b = start.pop()
                    for k in range(4):
                        nx = a + dx[k]; ny = b + dy[k]
                        if 0 <= nx < N and 0 <= ny < M:
                            if matrix[nx][ny] != 0 and not visit[nx][ny]:
                                visit[nx][ny] = True
                                start.append((nx, ny))
    if all >= 2:
        print(final)
        break
    year = [[0] * M for _ in range(N)]
    for x in range(N):
        for y in range(M):
            if matrix[x][y] != 0:
                cnt = 0
                for k in range(4):
                    nx = x + dx[k]; ny = y + dy[k]
                    if 0 <= nx < N and 0 <= ny < M:
                        if matrix[nx][ny] == 0:
                            cnt += 1
                if matrix[x][y] - cnt < 0:
                    year[x][y] = 0
                else:
                    year[x][y] = matrix[x][y] - cnt
    final += 1
    matrix = year
else:
    print(0)