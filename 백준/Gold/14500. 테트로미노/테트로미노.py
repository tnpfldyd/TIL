import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
res = 0
dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def dfs(x, y, depth, total):
    global res
    if depth == 4:
        res = max(res, total)
        return
    for dx, dy in dirs:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
            visited[nx][ny] = True
            dfs(nx, ny, depth + 1, total + board[nx][ny])
            visited[nx][ny] = False

for i in range(N):
    for j in range(M):
        visited[i][j] = True
        dfs(i, j, 1, board[i][j])
        visited[i][j] = False
        for k in range(4):
            s = board[i][j]
            cnt = 0
            for l in range(3):
                d = (k + l) % 4
                nx, ny = i + dirs[d][0], j + dirs[d][1]
                if 0 <= nx < N and 0 <= ny < M:
                    s += board[nx][ny]
                    cnt += 1
            if cnt == 3:
                res = max(res, s)

print(res)