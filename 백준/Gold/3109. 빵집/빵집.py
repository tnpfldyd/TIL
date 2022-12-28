import sys
input = sys.stdin.readline
N, M = map(int, input().split())

matrix = [list(input().strip()) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
result = 0
dx = [-1, 0, 1]
def dfs(x, y):
    if y == M-1:
        return True
    for i in range(3):
        nx = x + dx[i]
        if 0 <= nx < N and not visited[nx][y+1] and matrix[nx][y+1] == '.':
            visited[nx][y+1] = True
            if dfs(nx, y+1):
                return True
    return False
for i in range(N):
    if matrix[i][0] == '.':
        if dfs(i, 0):
            result += 1
print(result)