from collections import deque
import sys
input = sys.stdin.readline
N, M = map(int,input().split())
matrix = [list(map(int, input().rstrip().split())) for _ in range(N)]
result = []
dx, dy = [0,0,1,-1],[1,-1,0,0]
max_cnt = 0
for i in range(N):
    for j in range(M):
        if matrix[i][j] != 0:
            visited = [[-1]*M for _ in range(N)]
            start = deque()
            start.append((i, j))
            visited[i][j] = 0
            while start:
                x, y = start.popleft()
                for k in range(4):
                    nx, ny = x + dx[k], y + dy[k]
                    if 0 <= nx < N and 0 <= ny < M:
                        if matrix[nx][ny] != 0 and visited[nx][ny] == -1:
                            visited[nx][ny] = visited[x][y] + 1
                            start.append((nx, ny))
            
            cnt = max(map(max, visited))
            if max_cnt < cnt:
                max_cnt = cnt
            result.append((i,j,x,y,cnt))
result_cnt = 0
for i in result:
    if i[4] == max_cnt:
        if result_cnt < matrix[i[0]][i[1]] + matrix[i[2]][i[3]]:
            result_cnt = matrix[i[0]][i[1]] + matrix[i[2]][i[3]]
print(result_cnt)