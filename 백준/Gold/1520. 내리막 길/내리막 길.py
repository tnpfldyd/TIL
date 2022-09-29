import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
visited = [[-1] * M for _ in range(N)]
dx, dy = [0,0,1,-1], [1,-1,0,0]
def bfs(x, y):
    if x == N - 1 and y == M - 1:
        return 1
    if visited[x][y] != -1:
        return visited[x][y]
    visited[x][y] = 0
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < N and 0 <= ny < M and matrix[x][y] > matrix[nx][ny]:
            visited[x][y] += bfs(nx, ny)
    return visited[x][y]
print(bfs(0, 0))