from collections import deque
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
matrix = [list(map(int, input().strip().split())) for _ in range(N)]
dx, dy = [0,0,1,-1], [1,-1,0,0]
cnt = 0
while True:
    one_dic = {}
    visited = [[False] * M for _ in  range(N)]
    start = deque()
    start.append((0, 0))
    visited[0][0] = True
    while start:
        x, y = start.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                if matrix[nx][ny] == 0:
                    visited[nx][ny] = True
                    start.append((nx, ny))
                else:
                    if (nx, ny) not in one_dic:
                        one_dic[(nx, ny)] = 1
                    else:
                        one_dic[(nx, ny)] += 1
    if not len(one_dic):
        break
    else:
        for k, v in one_dic.items():
            if v >= 2:
                matrix[k[0]][k[1]] = 0
        cnt += 1
print(cnt)