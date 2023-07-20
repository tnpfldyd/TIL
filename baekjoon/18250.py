import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)
N, M = map(int, input().split())

in_degree = [0] * (N + 1)
matrix = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    matrix[a].append(b)
    matrix[b].append(a)
    in_degree[a] += 1; in_degree[b] += 1

visited = [False] * (N + 1)
answer = 0

def dfs(node):
    visited[node] = True
    if in_degree[node] == 0:
        return -1
    cnt = 0
    if in_degree[node] % 2:
        cnt += 1

    for next_node in matrix[node]:
        if not visited[next_node]:
            cnt += dfs(next_node)
    return cnt

for i in range(1, N + 1):
    if not visited[i]:
        result = dfs(i)
        if result == -1:
            continue
        if not result:
            answer += 1
        else:
            answer += result//2
print(answer)