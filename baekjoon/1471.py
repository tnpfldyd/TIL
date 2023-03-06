from collections import defaultdict
from heapq import heappop, heappush
import sys
sys.setrecursionlimit(10 ** 7)

N = int(input())
matrix = defaultdict(list)
rev_matrix = defaultdict(list)

for i in range(1, N+1):
    now = str(i)
    next = 0
    for j in range(len(now)):
        next += int(now[j])
    if next + i > N:
        if not (next + i) % N :
            matrix[i].append(i)
            rev_matrix[i].append(i)
        else:
            matrix[i].append((next + i) % N) 
            rev_matrix[(next + i) % N].append(i)
    else:
        matrix[i].append(next + i)
        rev_matrix[next + i].append(i)

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

visited = [False] * (N + 1)
stack = []
for i in range(1, N + 1):
    if not visited[i]:
        dfs(i)

scc = [-1] * (N + 1)
cnt = 0
scc_result = []
while stack:
    node = stack.pop()
    if scc[node] == -1:
        temp = []
        rev_dfs(node)
        cnt += 1
        scc_result.append(temp)

in_degree = [0] * cnt
scc_matrix = defaultdict(set)
for i in range(1, N + 1):
    for j in matrix[i]:
        if scc[i] != scc[j]:
            scc_matrix[scc[i]].add(scc[j])
            in_degree[scc[j]] += 1

answer = 0
visited = [0] * cnt
start = []
for i in range(cnt):
    if not in_degree[i]:
        heappush(start, (-len(scc_result[i]), i))
        visited[i] = len(scc_result[i])
while start:
    size, node = heappop(start)
    answer = max(answer, -size)
    for next in scc_matrix[node]:
        nx = visited[node] + len(scc_result[next])
        if visited[next] < nx:
            visited[next] = nx
        in_degree[next] -= 1
        if not in_degree[next]:
            heappush(start, (-visited[next], next))
print(answer)