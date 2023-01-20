N, M, K = map(int, input().split())

jewel = [0] * (N + 1)
for i in range(1, K + 1):
    number = int(input())
    jewel[number] = i

matrix = [[] for _ in range(N + 1)]
visited = [[False] * (1 << K + 1) for _ in range(N + 1)]
for _ in range(M):
    a, b, cost = map(int, input().split())
    matrix[a].append((cost, b))
    matrix[b].append((cost, a))
matrix[1].append((15, 1))
answer = 0
def dfs(node, bit, cnt):
    global answer
    visited[node][bit] = True
    if node == 1:
        answer = max(answer, cnt)
    for max_cost, i in matrix[node]:
        if max_cost >= cnt and not visited[i][bit]:
            dfs(i, bit, cnt)
        if jewel[i]:
            if bit & 1 << jewel[i]:
                continue
            if max_cost >= cnt + 1 and not visited[i][bit | 1 << jewel[i]]:
                dfs(i, bit | 1 << jewel[i], cnt + 1)
dfs(1, 0 ,0)
print(answer)