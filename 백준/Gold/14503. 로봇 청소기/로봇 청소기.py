import sys
input = sys.stdin.readline
N, M = map(int, input().split())
x, y, dir = map(int, input().split())
dx, dy = [-1,0,1,0], [0,1,0,-1]
matrix = [list(map(int, input().strip().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
visited[x][y] = True
while True:
    for _ in range(4):
        nx, ny = x + dx[(dir+3)%4], y + dy[(dir+3)%4]
        dir = (dir+3)% 4
        if 0 <= nx < N and 0 <= ny < M:
            if not visited[nx][ny] and not matrix[nx][ny]:
                visited[nx][ny] = True
                x, y = nx, ny
                break
    else:
        nx, ny = x - dx[dir], y - dy[dir]
        if matrix[nx][ny]:
            break
        x, y = nx, ny
print(sum(map(sum, visited)))