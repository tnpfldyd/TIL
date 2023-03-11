import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

N, R, M = map(int, input().split())
board = [(0, 0)]
for _ in range(M):
    a, b = map(int, input().split())
    board.append((a, b))

def meet(i, j):
    if board[i][0] == board[j][0]:
        if abs(board[i][1] - board[j][1]) <= 2 * R:
            return 1
    elif board[i][1] == board[j][1]:
        if abs(board[i][0] - board[j][0]) <= 2 * R:
            return 2
    return 0

matrix = [[] for _ in range(2 * M + 1)]
rev_matrix = [[] for _ in range(2 * M + 1)]
for i in range(1, M + 1):
    for j in range(i + 1, M + 1):
        m = meet(i, j)
        if m == 1:
            matrix[i].append(-j)
            matrix[j].append(-i)
            rev_matrix[-j].append(i)
            rev_matrix[-i].append(j)
        elif m == 2:
            matrix[-i].append(j)
            matrix[-j].append(i)
            rev_matrix[j].append(-i)
            rev_matrix[i].append(-j)

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

visited = [False] * (2 * M + 1)
stack = []

for i in range(1, 2 * M + 1):
    if not visited[i]:
        dfs(i)

cnt = 0
scc = [-1] * (2 * M + 1)
while stack:
    n = stack.pop()
    if scc[n] == -1:
        rev_dfs(n)
        cnt += 1
for i in range(1, M + 1):
    if scc[i] == scc[-i]:
        print(0)
        break
else:
    print(1)