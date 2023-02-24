from collections import defaultdict
import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def add_edge(x, y):
    matrix[-x].append(y)
    matrix[-y].append(x)

def dfs(x):
    global cnt, scc_cnt
    cnt += 1
    visited[x] = cnt
    ret = cnt
    stack.append(x)
    for next in matrix[x]:
        if not visited[next]:
            ret = min(ret, dfs(next))
        elif not scc[next]:
            ret = min(ret, visited[next])
    if ret == visited[x]:
        scc_cnt += 1
        while True:
            node = stack.pop()
            scc[node] = scc_cnt
            if node == x:
                break

    return ret

N, M = map(int, input().split())
matrix = defaultdict(list)
for i in range(1, N + 1):
    board = input()
    for j in range(M):
        if board[j] == '.':
            continue
        J = j + N + 1
        if board[j] == '#':
            add_edge(i, -J)
            add_edge(-i, J)
        elif board[j] == '*':
            add_edge(i, J)
            add_edge(-i, -J)

visited = [0] * (2 * (N + M) + 1)
scc = [0] * (2 * (N + M) + 1)
cnt, scc_cnt = 0, 0
stack = []
for i in range(1, 2 * (N + M) + 1):
    if not visited[i]:
        dfs(i)

for i in range(1, N + M + 1):
    if scc[i] == scc[-i]:
        print(0)
        break
else:
    print(1)