from pprint import pprint
import sys
def dfs(x, y):
    if x == 0:
        return print(f'#{i} {y}')
    global s
    if s == 2:
        for j in range(2):
            nx = x + dx[j]; ny = y + dy[j]
            if 0 <= ny < 100 and matrix[nx][ny] == 1:
                s = j
                dfs(nx, ny)
                break
        else:
            nx = x + dx[s]; ny = y + dy[s]
            dfs(nx, ny)
    elif s == 1 or s == 0:
        if 0 <= y + dy[s] < 100 and matrix[x + dx[s]][y + dy[s]] == 1:
            nx = x + dx[s]; ny = y + dy[s]
            dfs(nx, ny)
        else:
            s = 2
            nx = x + dx[s]; ny = y + dy[s]
            dfs(nx, ny)


sys.stdin = open('1210input.txt', 'r')
T = 10
for i in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(100)]
    dx, dy = [0, 0, -1], [-1, 1, 0]
    s = 2
    start = []
    for k in range(100):
        if matrix[99][k] == 2:
            dfs(99, k)
    # while start:
    #     x, y = start.pop()
    #     if x == 0:
    #         print(f'#{i} {y}')
    #         break
    #     if s == 2:
    #         for j in range(2):
    #             nx = x + dx[j]; ny = y + dy[j]
    #             if 0 <= ny < 100 and matrix[nx][ny] == 1:
    #                 s = j
    #                 start.append((nx, ny))
    #                 break
    #         else:
    #             nx = x + dx[s]; ny = y + dy[s]
    #             start.append((nx, ny))
    #     elif s == 1 or s == 0:
    #         if 0 <= y + dy[s] < 100 and matrix[x + dx[s]][y + dy[s]] == 1:
    #             nx = x + dx[s]; ny = y + dy[s]
    #             start.append((nx, ny))
    #         else:
    #             s = 2
    #             nx = x + dx[s]; ny = y + dy[s]
    #             start.append((nx, ny))