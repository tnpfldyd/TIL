import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

N, R, Q = map(int, input().split())
matrix = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    u, v= map(int, input().split())
    matrix[u].append(v)
    matrix[v].append(u)

tree = [0] * (N + 1)
visited = [False] * (N + 1)
def dfs(cur):
    if tree[cur]: return tree[cur]
    ret = 1
    visited[cur] = True
    for nxt in matrix[cur]:
        if visited[nxt]: continue
        ret += dfs(nxt)
    tree[cur] = ret
    return ret

dfs(R)

for _ in range(Q):
    print(tree[int(input())])