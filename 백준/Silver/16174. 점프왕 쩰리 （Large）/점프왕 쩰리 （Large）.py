import sys
input = sys.stdin.readline
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]
dx, dy = [1, 0], [0, 1]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def dfs(x, y):
    visited[x][y] = True
    for i in range(2):
        nx, ny = x + dx[i] * graph[x][y], y + dy[i] * graph[x][y]
        if in_range(nx, ny) and not visited[nx][ny]:
            if graph[nx][ny] == -1:
                print("HaruHaru")
                exit(0)
            else:
                dfs(nx, ny)
    return False

if not dfs(0, 0):
    print("Hing")