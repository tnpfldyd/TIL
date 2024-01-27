dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]

N, *percent = map(int, input().split())
visited = [[False] * 29 for _ in range(29)]

def dfs(x, y, cnt):
    if cnt == N:
        return 1
    visited[x][y] = True
    result = 0
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if visited[nx][ny]: continue
        result += percent[i] / 100 * dfs(nx, ny, cnt + 1)
    visited[x][y] = False
    return result

answer = dfs(14, 14, 0)
print(answer)