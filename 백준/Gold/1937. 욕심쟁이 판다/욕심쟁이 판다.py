import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
def dfs(x, y):
    if visited[x][y] == -1:
        visited[x][y] = 0
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if matrix[nx][ny] > matrix[x][y]:
                    visited[x][y] = max(visited[x][y], dfs(nx, ny))
    return visited[x][y]+1

dx, dy = [0,1,0,-1],[1,0,-1,0]
N = int(input())
matrix = [list(map(int, input().rstrip().split())) for _ in range(N)]
visited = [[-1] * N for _ in range(N)]
cnt = 0
for x in range(N):
    for y in range(N):
        cnt = max(cnt, dfs(x, y))
print(cnt)