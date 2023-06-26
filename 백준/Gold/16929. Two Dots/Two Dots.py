import sys
input = sys.stdin.readline
N, M = map(int, input().split())

matrix = [list(input().strip()) for _ in range(N)]
dx, dy = [0,0,1,-1],[1,-1,0,0]
visited = [[False] * M for _ in range(N)]
answer = False
def dfs(x, y, bx, by):
    if visited[x][y]:
        return True
    visited[x][y] = True
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if (nx, ny) != (bx, by) and 0 <= nx < N and 0 <= ny < M and matrix[x][y] == matrix[nx][ny]:
            if dfs(nx, ny, x, y):
                return True
    return False

for i in range(N):
    for j in range(M):
        if not visited[i][j] and not answer:
            if dfs(i, j, -1, -1):
                answer = True
print("Yes" if answer else "No")