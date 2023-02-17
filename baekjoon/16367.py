import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)
N, M = map(int, input().split())
matrix = [[] for _ in range(2 * N + 1)]
rev_matrix = [[] for _ in range(2 * N + 1)]
def edge(x, y):
    matrix[-x].append(y)
    matrix[-y].append(x)
    rev_matrix[y].append(-x)
    rev_matrix[x].append(-y)

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

for _ in range(M):
    order = []
    order_list = input().strip().split()
    for i in range(0, 5, 2):
        temp = int(order_list[i])
        if order_list[i+1] == 'R':
            temp = -temp
        order.append(temp)
    a, b, c = order
    edge(a, b); edge(b, c); edge(c, a)

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
for i in range(1, N + 1):
    if scc[i] == scc[-i]:
        print(-1)
        break
    else:
        answer.append('B') if scc[i] > scc[-i] else answer.append('R')
else:
    print(''.join(answer))