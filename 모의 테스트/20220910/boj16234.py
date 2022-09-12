from collections import deque
import sys
input = sys.stdin.readline
N, L, H = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
dx, dy = [0,0,1,-1], [1,-1,0,0]
answer = True
cnt = 0
while answer:
    tem = 0
    visited = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                visited[i][j] = True
                start = deque()
                result = []
                temp = []
                start.append((i, j))
                result.append(matrix[i][j])
                temp.append((i, j))
                while start:
                    x, y = start.popleft()
                    for k in range(4):
                        nx, ny = x + dx[k], y + dy[k]
                        if 0 <= nx < N and 0 <= ny < N:
                            if not visited[nx][ny] and L <= abs(matrix[x][y] - matrix[nx][ny]) <= H:
                                visited[nx][ny] = True
                                start.append((nx, ny))
                                result.append(matrix[nx][ny])
                                temp.append((nx, ny))
                                tem += 1
                if len(result) > 1:
                    result_sum = sum(result)//len(temp)
                    for k1, k2 in temp:
                        matrix[k1][k2] = result_sum
    if tem > 0:
        cnt += 1
    else:
        answer = False
print(cnt)