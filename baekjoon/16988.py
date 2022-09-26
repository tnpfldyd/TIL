from collections import deque
import itertools, sys
input = sys.stdin.readline
N, M = map(int, input().split())
matrix = [list(map(int, input().rstrip().split())) for _ in range(N)]
two = []
one = []
zero = []
dx, dy = [0,0,1,-1],[1,-1,0,0]
for i in range(N):
    for j in range(M):
        if matrix[i][j] == 0:
            zero.append((i, j))
        elif matrix[i][j] == 1:
            one.append((i, j))
        else:
            two.append((i, j))
max_cnt = 0
for num1, num2 in itertools.combinations(zero, 2):
    matrix[num1[0]][num1[1]] = 1
    matrix[num2[0]][num2[1]] = 1
    visited = [[False] * M for _ in range(N)]
    cnt = 0
    for i in two:
        if not visited[i[0]][i[1]]:
            temp = 0
            start = deque()
            start.append(i)
            visited[i[0]][i[1]] = True
            temp += 1
            answer = True
            while start:
                x, y = start.popleft()
                for k in range(4):
                    nx, ny = x + dx[k], y + dy[k]
                    if 0 <= nx < N and 0 <= ny < M:
                        if matrix[nx][ny] == 2 and not visited[nx][ny]:
                            visited[nx][ny] = True
                            temp += 1
                            start.append((nx, ny))
                        elif matrix[nx][ny] == 0:
                            answer = False
            if answer:
                cnt += temp
    if cnt > max_cnt:
        max_cnt = cnt
    matrix[num1[0]][num1[1]] = 0
    matrix[num2[0]][num2[1]] = 0
print(max_cnt)