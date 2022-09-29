import sys
input = sys.stdin.readline
def dfs(x, y, temp):
    global cnt
    cnt = max(temp, cnt)
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if not visited[matrix[nx][ny]]:
                visited[matrix[nx][ny]] = True
                dfs(nx, ny, temp + 1)
                visited[matrix[nx][ny]] = False
dx, dy = [0,1,0,-1],[1,0,-1,0]
N, M = map(int, input().split())
matrix = [list(map(lambda x : ord(x) - 65, input().rstrip())) for _ in range(N)]
visited = [False] * 26
cnt = 0
visited[matrix[0][0]] = True
dfs(0, 0, 1)
print(cnt)