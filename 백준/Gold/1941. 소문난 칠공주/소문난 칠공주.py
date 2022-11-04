from collections import deque
import itertools, sys
input = sys.stdin.readline
matrix = [list(input().strip()) for _ in range(5)]
list_ = []
for i in range(5):
    for j in range(5):
        list_.append((i, j))
dx, dy = [0,0,1,-1], [1,-1,0,0]
cnt = 0
for i in itertools.combinations(list_, 7):
    check = 0
    for j in i:
        if matrix[j[0]][j[1]] == 'S':
            check += 1
    if check < 4:
        continue
    visited = [[False] * 5 for _ in range(5)]
    for j in i:
        visited[j[0]][j[1]] = True
    start = deque()
    start.append((i[0][0], i[0][1]))
    visited[i[0][0]][i[0][1]] = False
    while start:
        x, y = start.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < 5 and 0 <= ny < 5:
                if visited[nx][ny]:
                    visited[nx][ny] = False
                    start.append((nx, ny))
    if not sum(map(sum, visited)):
        cnt += 1
print(cnt)