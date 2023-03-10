from collections import deque
import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

N, M = map(int, input().split())
matrix = [[] for _ in range(N + 1)]
rev_matrix = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    matrix[a].append(b)
    rev_matrix[b].append(a)

def dfs(x):
    visited[x] = True
    for i in matrix[x]:
        if not visited[i]:
            dfs(i)
    stack.append(x)

def rev_dfs(x):
    scc[x] = cnt
    for i in rev_matrix[x]:
        if scc[i] == -1:
            rev_dfs(i)

visited = [False] * (N + 1)
stack = []
for i in range(1, N + 1):
    if not visited[i]:
        dfs(i)

scc = [-1] * (N + 1)
cnt = 0
while stack:
    node = stack.pop()
    if scc[node] == -1:
        rev_dfs(node)
        cnt += 1

scc_matrix = [[] for _ in range(cnt)]
in_degree = [0] * cnt
for i in range(1, N + 1):
    for j in matrix[i]:
        if scc[i] != scc[j]:
            scc_matrix[scc[i]].append(scc[j])
            in_degree[scc[j]] += 1

start = deque()
temp = -1
for i in range(cnt):
    if not in_degree[i]:
        start.append(i)
        temp = i

if len(start) == 1:
    result = []
    while start:
        x = start.popleft()
        result.append(x)
        next_cnt = 0
        for i in scc_matrix[x]:
            in_degree[i] -= 1
            if not in_degree[i]:
                start.append(i)
                next_cnt += 1
        if next_cnt > 1:
            result = []
            break
    if len(result) == cnt:
        answer = []
        for i in range(1, N + 1):
            if scc[i] == temp:
                answer.append(i)
        print(len(answer))
        print(*answer)
    else:
        print(0)
else:
    print(0)