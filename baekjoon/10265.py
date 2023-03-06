import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

N, K = map(int, input().split())
bus = [0] + list(map(int, input().split()))
matrix = [[] for _ in range(N + 1)]
rev_matrix = [[] for _ in range(N + 1)]
for i in range(1, N + 1):
    matrix[bus[i]].append(i)
    rev_matrix[i].append(bus[i])

def dfs(x):
    visited[x] = True
    for next in matrix[x]:
        if not visited[next]:
            dfs(next)
    stack.append(x)

def rev_dfs(x):
    scc[x] = cnt
    temp.append(x)
    for next in rev_matrix[x]:
        if scc[next] == -1:
            rev_dfs(next)

def make(idx, root, parent):
    visited[idx] = True
    ret = 0
    if root:
        ret = min_max[cnt][0] = len(scc_group[scc[idx]])

    if scc[idx] != parent:
        ret = len(scc_group[scc[idx]])

    for next in matrix[idx]:
        if not visited[next]:
            ret += make(next, False, scc[idx])

    if root:
        min_max[cnt][1] = ret

    return ret

stack = []
visited = [False] * (N + 1)

for i in range(1, N + 1):
    if not visited[i]:
        dfs(i)

scc_group = []
scc = [-1] * (N + 1)
cnt = 0
while stack:
    node = stack.pop()
    if scc[node] == -1:
        temp = []
        rev_dfs(node)
        cnt += 1
        scc_group.append(temp)

in_degree = [0] * cnt

for i in range(1, N + 1):
    for j in matrix[i]:
        if scc[i] != scc[j]:
            in_degree[scc[j]] += 1
visited = [False] * (N + 1)
cnt = 0
min_max = []
for i in range(1, N + 1):
    if not in_degree[scc[i]] and not visited[i]:
        min_max.append([0, 0])
        make(i, True, scc[i])
        cnt += 1

dp = [[0] * (K + 1) for _ in range(len(min_max))]

for i in range(len(min_max)):
    min_cnt, max_cnt = min_max[i][0], min_max[i][1]
    if min_cnt > K:
        continue
    for j in range(K, -1, -1):
        dp[i][j] = dp[i - 1][j]
        for k in range(min_cnt, max_cnt + 1):
            if j - k >= 0:
                dp[i][j] = max(dp[i][j], dp[i - 1][j - k] + k)

print(max(dp[cnt - 1]))