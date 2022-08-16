import sys
sys.stdin = open('1211input.txt', 'r')
def dfs(x, y):
    global cnt; global s
    dx, dy = [0, 0, 1], [1, -1, 0]
    if x == 99:
        return
    if s == 2:
        for i in range(2):
            nx = x + dx[i]; ny = y + dy[i]
            if 0 <= ny < 100 and matrix[nx][ny] == 1:
                s = i
                cnt += 1
                dfs(nx, ny)
                break
        else:
            nx = x + dx[s]; ny = y + dy[s]
            cnt += 1
            dfs(nx, ny)
    elif s == 1 or s == 0:
        if 0 <= y + dy[s] < 100 and matrix[x + dx[s]][y + dy[s]] == 1:
            cnt += 1      
            dfs(x + dx[s], y + dy[s])
        else:
            s = 2
            cnt += 1
            dfs(x + dx[s], y + dy[s])
            
T = 10
for i in range(1, T+1):
    num = int(input())
    matrix = [list(map(int, input().split())) for _ in range(100)]
    result = {}
    cnt = 0
    s = 2
    for j in range(100):
        if matrix[0][j] == 1:
            dfs(0, j)
            result[j] = cnt
            cnt = 0
    min_result = [k for k, v in result.items() if min(result.values()) == v]
    print(f'#{num} {min_result[0]}')