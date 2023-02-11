import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)
N = int(input())
hash_dic = {}
matrix = []
rev_matrix = []
cnt = -1
for _ in range(N):
    orders = input().strip().split()
    temp = []
    if orders[0] not in hash_dic:
        cnt += 1
        matrix.append([])
        rev_matrix.append([])
        hash_dic[orders[0]] = cnt
    for i in range(int(orders[1])):
        if orders[i + 2] not in hash_dic:
            cnt += 1
            matrix.append([])
            rev_matrix.append([])
            hash_dic[orders[i + 2]] = cnt
        matrix[hash_dic[orders[i + 2]]].append(hash_dic[orders[0]])
        rev_matrix[hash_dic[orders[0]]].append(hash_dic[orders[i + 2]])
cnt += 1

def dfs(x):
    if visited[x]:
        return
    visited[x] = True
    for next in matrix[x]:
        if not visited[next]:
            dfs(next)
    stack.append(x)

visited = [False] * cnt
stack = []
for i in range(cnt):
    if not visited[i]:
        dfs(i)

def rev_dfs(x):
    if scc[x] != -1:
        return
    scc[x] = scc_cnt
    for next in rev_matrix[x]:
        if scc[next] == -1:
            rev_dfs(next)
target = hash_dic[input().strip()]
scc_cnt = 0
scc = [-1] * cnt
while stack:
    node = stack.pop()
    if scc[node] == -1:
        rev_dfs(node)
        scc_cnt += 1
scc_matrix = [[] for _ in range(cnt)]
in_degree = [0] * cnt
for i in range(cnt):
    for j in matrix[i]:
        if scc[i] != scc[j]:
            scc_matrix[i].append(j)
            in_degree[j] += 1
cost = [1] * cnt
stack = []
for i in range(cnt):
    if not in_degree[i]:
        stack.append(i)

while stack:
    x = stack.pop()
    for next in scc_matrix[x]:
        cost[next] += cost[x]
        in_degree[next] -= 1
        if not in_degree[next]:
            stack.append(next)
print(cost[target])