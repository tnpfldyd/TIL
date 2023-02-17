import sys
# sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

T = int(input())
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

for case in range(T):
    input()
    N = int(input())
    board = [list(map(int,input().strip())) for _ in range(N)]
    for i in range(N):
        board[i][i] = 0
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if board[i][j] and board[i][k] and board[k][j]:
                    board[i][j] = 0
    matrix = [[] for _ in range(N)]
    rev_matrix = [[] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if board[i][j]:
                matrix[i].append(j)
                rev_matrix[j].append(i)
    visited = [False] * N
    stack = []
    for i in range(N):
        if not visited[i]:
            dfs(i)

    scc = [-1] * N
    cnt = 0
    answer = []
    while stack:
        node = stack.pop()
        temp = []
        if scc[node] == -1:
            rev_dfs(node)
            cnt += 1
        if len(temp) == 1 or not temp:
            continue
        for i in range(len(temp) - 1):
            answer.append((temp[i] + 1, temp[i + 1] + 1))
        answer.append((temp[-1] + 1, temp[0] + 1))
    for i in range(N):
        for j in matrix[i]:
            if scc[i] != scc[j]:
                answer.append((i + 1, j + 1))
    print(len(answer))
    for i in answer:
        print(*i)
    if case != T - 1:
        print()