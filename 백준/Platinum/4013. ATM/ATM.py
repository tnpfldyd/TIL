from collections import deque
import sys
input = sys.stdin.readline
INF = sys.maxsize
sys.setrecursionlimit(10 ** 7)

def dfs(x):
    if visited[x]:
        return
    visited[x] = True
    for i in matrix[x]:
        if not visited[i]:
            dfs(i)
    stack.append(x)

def rev_dfs(x):
    scc[x] = cnt
    if cnt not in depth:
        depth[cnt] = 1
        money[cnt] = money_list[x]
    else:
        depth[cnt] += 1
        money[cnt] += money_list[x]
    for i in rev_matrix[x]:
        if scc[i] == -1:
            rev_dfs(i)

N, M = map(int, input().split())
matrix = [[] for _ in range(N)]
rev_matrix = [[] for _ in range(N)]


for _ in range(M):
    a, b = map(int, input().split())
    a -= 1; b -= 1
    matrix[a].append(b)
    rev_matrix[b].append(a)

visited = [False] * N
stack = []

for i in range(N):
    if not visited[i]:
        dfs(i)

cnt = 0
scc = [-1] * N
depth = {}
money = {}
money_list = [int(input().strip()) for _ in range(N)]
while stack:
    node = stack.pop()
    if scc[node] == -1:
        rev_dfs(node)
        cnt += 1

scc_adj = [[] for _ in range(cnt)]

for i in range(N):
    for j in matrix[i]:
        if scc[i] != scc[j]:
            scc_adj[scc[i]].append(scc[j])
S, P = map(int, input().split())
S -= 1
restaurants = tuple(map(int, input().split()))
start = deque()
start.append(scc[S])
visited = [0] * cnt
visited[scc[S]] = money[scc[S]]
while start:
    x = start.popleft()
    for i in scc_adj[x]:
        nx = visited[x] + money[i]
        if visited[i] < nx:
            visited[i] = nx
            start.append(i)
answer = 0
for restaurant in restaurants:
    if answer < visited[scc[restaurant-1]]:
        answer = visited[scc[restaurant-1]]
print(answer)