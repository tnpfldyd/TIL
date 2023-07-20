import sys
INF = sys.maxsize
input = sys.stdin.readline

N = int(input())
M = (N + 1) * 10
a_graph = [list(map(lambda x : int(x) if x != '.' else 0, input().strip())) for _ in range(N)]
b_graph = [list(map(lambda x : int(x) if x != '.' else 0, input().strip())) for _ in range(N)]

dp = [[[-1] * M for _ in range(M)] for _ in range(N + 1)]

def dfs(node, a, b):
    if dp[node][a][b] != -1:
        return dp[node][a][b]
    if node == 1:
        dp[node][a][b] = 1
        return 1
    dp[node][a][b] = 0
    for i in range(N):
        if a_graph[node][i] and b_graph[node][i]:
            next_a, next_b = a + a_graph[node][i] , b + b_graph[node][i]
            if next_a < M and next_b < M:
                dp[node][a][b] = max(dp[node][a][b], dfs(i, next_a, next_b))
    return dp[node][a][b]

if not dfs(0, 0, 0):
    print(-1)
else:
    answer = INF
    for i in range(M):
        for j in range(M):
            if dp[1][i][j] == 1:
                answer = min(answer, i * j)
    print(answer)