import sys
input = sys.stdin.readline

def dfs(x):
    visited[x] = True
    for i in matrix[x]:
        if not visited[i]:
            dfs(i)
    stack.append(x)

def rev_dfs(x):
    temp.append(x)
    scc[x] = cnt
    for i in rev_matrix[x]:
        if scc[i] == -1:
            rev_dfs(i)

def getresult(scc_list_x):
    temp = 0
    for i in range(len(scc_list_x)):
        idx = scc_list_x[i]
        cur = 1 - percent[idx]
        for j in range(i):
            prev = scc_list_x[j]
            cur *= percent[prev]
        temp += cur
    return temp

while True:
    N = int(input())
    if not N:
        break
    matrix = [[] for _ in range(N + 1)]
    rev_matrix = [[] for _ in range(N + 1)]
    percent = [0] * (N + 1)
    for i in range(1, N + 1):
        next_line = input().split()
        percent[i] = float(next_line[0])
        for j in range(2, int(next_line[1]) + 2):
            v = int(next_line[j])
            matrix[i].append(v)
            rev_matrix[v].append(i)
    visited = [False] * (N + 1)
    stack = []
    for i in range(1, N + 1):
        if not visited[i]:
            dfs(i)
    scc = [-1] * (N + 1)
    cnt = 0
    scc_list = []
    while stack:
        n = stack.pop()
        if scc[n] == -1:
            temp = []
            rev_dfs(n)
            cnt += 1
            scc_list.append(temp)
    
    in_degree = [0] * cnt
    for i in range(1, N + 1):
        for j in matrix[i]:
            if scc[i] != scc[j]:
                in_degree[scc[j]] += 1
    result = 1
    for i in range(cnt):
        if not in_degree[i]:
            result *= getresult(scc_list[i])
    print(f"{result:.9f}")