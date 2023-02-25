import sys
input = sys.stdin.readline

def dfs(x):
    visited[x] = True
    for next in matrix[x]:
        if not visited[next]:
            dfs(next)
    stack.append(x)

def rev_dfs(x):
    scc[x] = cnt
    temp.append(chr(x + 65))
    for next in rev_matrix[x]:
        if scc[next] == -1:
            rev_dfs(next)

while True:
    N = int(input())
    if not N:
        break
    matrix = [[] for _ in range(26)]
    rev_matrix = [[] for _ in range(26)]
    alpha = [False] * 26
    for _ in range(N):
        orders = list(map(lambda x : ord(x) - 65, input().split()))
        for i in range(5):
            alpha[orders[i]] = True
            if orders[5] == orders[i]:
                continue
            matrix[orders[5]].append(orders[i])
            rev_matrix[orders[i]].append(orders[5])
    visited = [False] * 26
    stack = []
    for i in range(26):
        if not visited[i]:
            dfs(i)
    scc = [-1] * 26
    cnt = 0
    result = []
    while stack:
        node = stack.pop()
        if scc[node] == -1:
            temp = []
            rev_dfs(node)
            cnt += 1
            temp.sort()
            result.append(temp)
    result.sort()
    for i in result:
        if len(i) == 1 and not alpha[ord(i[0])-65]:
            continue
        print(*i)
    print()