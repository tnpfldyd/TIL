import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

def transX(a):
    if a[-1] == 'h':
        return int(a[:-1]) + 1
    else:
        return -int(a[:-1]) - 1

def dfs(x):
    visited[x] = True
    for next in matrix[x]:
        if not visited[next]:
            dfs(next)
    stack.append(x)

def rev_dfs(x):
    scc[x] = cnt
    for next in rev_matrix[x]:
        if scc[next] == -1:
            rev_dfs(next)
while True:
    N, M = map(int, input().split())
    if (N, M) == (0, 0):
        break

    matrix = [[] for _ in range(2 * N + 1)]
    rev_matrix = [[] for _ in range(2 * N + 1)]

    for _ in range(M):
        x, y = input().strip().split()
        x, y = transX(x), transX(y)
        matrix[-x].append(y)
        matrix[-y].append(x)
        rev_matrix[y].append(-x)
        rev_matrix[x].append(-y)
    matrix[1].append(-1)
    rev_matrix[-1].append(1)
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
    answer = []
    for i in range(2, N + 1):
        if scc[i] == scc[-i]:
            print('bad luck')
            break
        else:
            if scc[i] > scc[-i]:
                answer.append(str(i-1)+'h')
            else:
                answer.append(str(i-1)+'w')
    else:
        print(*answer)