from collections import deque
import sys, itertools
input = sys.stdin.readline
N, M = map(int, input().split())
matrix = [list(map(int, input().rstrip().split())) for _ in range(N)]
two = []
onecnt = 0
for i in range(N):
    for j in range(N):
        if matrix[i][j] == 2:
            two.append((i, j))
            matrix[i][j] = '*'
        elif matrix[i][j] == 1:
            onecnt += 1
min_cnt = 987654321
dx, dy = [0,0,1,-1],[1,-1,0,0]
for i in itertools.combinations(two, M):
    start = deque()
    visit = [[-1]*N for _ in range(N)]
    for j in i:
        matrix[j[0]][j[1]] = 2
        visit[j[0]][j[1]] = 0
        start.append(j)
    temp = []
    while start:
        x, y = start.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < N and 0 <= ny < N:
                if matrix[nx][ny] == 0 and visit[nx][ny] == -1:
                    visit[nx][ny] = visit[x][y] + 1
                    start.append((nx, ny))
                elif matrix[nx][ny] == '*' and visit[nx][ny] == -1:
                    visit[nx][ny] = visit[x][y] + 1
                    start.append((nx, ny))
                    temp.append((nx, ny))
    cnt = 0
    max_cnt = 0
    for q in temp:
        visit[q[0]][q[1]] = 0
    for x in range(N):
        for y in range(N):
            if visit[x][y] == -1:
                cnt += 1
            else:
                if visit[x][y] > max_cnt:
                    max_cnt = visit[x][y]
    if cnt == onecnt:
        if min_cnt > max_cnt:
            min_cnt = max_cnt
    for j in i:
        matrix[j[0]][j[1]] = '*'
print(min_cnt if min_cnt != 987654321 else -1)