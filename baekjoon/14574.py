import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)
N = int(input())
parent = [0] * (N + 1)
temp = [(0, 0)]
for i in range(1, N + 1):
    parent[i] = i
    a, b = map(int, input().split())
    temp.append((b, a))
edges = []
for i in range(1, N + 1):
    for j in range(i + 1, N + 1):
        cost = int((temp[i][0] + temp[j][0]) / abs(temp[i][1] - temp[j][1]))
        edges.append((cost, i, j))

edges.sort(reverse=True)
def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x, y = find(x), find(y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y
answer = 0
matrix = [[] for _ in range(N + 1)]
for cost, a, b in edges:
    if find(a) != find(b):
        union(a, b)
        answer += cost
        matrix[a].append(b)
        matrix[b].append(a)
print(answer)
visited = [False] * (N + 1)
def dfs(cur_node):
    visited[cur_node] = True
    for next_node in matrix[cur_node]:
        if not visited[next_node]:
            dfs(next_node)
            print(cur_node, next_node)
dfs(1)