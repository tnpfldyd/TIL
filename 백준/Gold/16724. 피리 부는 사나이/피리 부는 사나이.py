import sys
input = sys.stdin.readline
dir = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}

def dfs(x, y):
    if info[x][y] == 0:
        return True
    elif info[x][y] == 1:
        return False

    c = info[x][y]
    info[x][y] = 0 
    res = dfs(x + dir[c][0], y + dir[c][1])
    info[x][y] = 1

    return res

N, M = map(int, input().split())

info = [list(input().strip()) for _ in range(N)]

count = 0
for i in range(N):
    for j in range(M):
        if dfs(i, j):
            count += 1

print(count)