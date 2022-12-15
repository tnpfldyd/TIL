import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def dfs(x, y, cnt):
    global result
    global answer
    result = max(result, cnt)
    for i in range(4):
        nx = x + int(matrix[x][y]) * dx[i]
        ny = y + int(matrix[x][y]) * dy[i]
        if 0 <= nx < N and 0 <= ny < M and matrix[nx][ny] != 'H' and cnt+1 > cntrix[nx][ny]:
            if not visited[nx][ny]:
                cntrix[nx][ny] = cnt + 1
                visited[nx][ny] = True
                dfs(nx, ny, cnt+1)
                visited[nx][ny] = False
            else:
                answer = True
N, M = map(int, input().split())
matrix = [list(input().strip()) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
cntrix = [[0] * M for _ in range(N)]
result = 0
dx, dy = [0,0,1,-1],[1,-1,0,0]
answer = False
dfs(0, 0, 1)
print(result if not answer else -1)