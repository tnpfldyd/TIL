import sys
input = sys.stdin.readline
def dfs(node, cnt, result):
    global final
    if cnt == N:
        final = min(final, result)
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            dfs(i, cnt + 1, result + matrix[node][i])
            visited[i] = False
N, s = map(int, input().split())
matrix = [list(map(int, input().strip().split())) for _ in range(N)]
for i in range(N):
    matrix[i][i] = 0
matrix2 = [[] for _ in range(N)]
for k in range(N):
    for i in range(N):
        for j in range(N):
            matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])
visited = [False] * N
visited[s] = True
final = sys.maxsize
dfs(s, 1, 0)
print(final)