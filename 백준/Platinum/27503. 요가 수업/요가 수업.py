import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

N, M, C, K = map(int, input().split())

check1 = [0] * (N + 1)
check2 = [0] * (N + 1)
graph = [[] for _ in range(2 * N + 1)]
rev_graph = [[] for _ in range(2 * N + 1)]

numbers = list(map(int, input().split()))

def addEdge(x, y):
    graph[-x].append(y)
    graph[-y].append(x)
    rev_graph[y].append(-x)
    rev_graph[x].append(-y)

def dfs(x):
    visited[x] = True
    for next_node in graph[x]:
        if not visited[next_node]:
            dfs(next_node)
    stack.append(x)

def rev_dfs(x):
    scc[x] = cnt
    for next_node in rev_graph[x]:
        if scc[next_node] == -1:
            rev_dfs(next_node)

for number in numbers:
    check1[number] = 1

for _ in range(C):
    a, b = map(int, input().split())
    addEdge(a, b)
    check2[a] = check2[b] = 1

for i in range(1, N + 1):
    if check1[i] and not check2[i]:
        addEdge(i, i)

for i in range(K):
    a, b = map(int, input().split())
    addEdge(-a, -b)

visited = [False] * (2 * N + 1)
stack = []

for i in range(1, 2 * N + 1):
    if not visited[i]:
        dfs(i)

scc = [-1] * (2 * N + 1)
cnt = 0

while stack:
    node = stack.pop()
    if scc[node] == -1:
        rev_dfs(node)
        cnt += 1

for i in range(1, N + 1):
    if scc[i] == scc[-i]:
        print("NO")
        break
else:
    print("YES")