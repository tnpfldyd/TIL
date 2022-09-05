import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline
N, M, start = map(int, input().split())
matrix = [[] for _ in range(N+1)]
visit = [0] * (N+1)
for i in range(M):
    a, b = map(int, input().split())
    matrix[a].append(b)
    matrix[b].append(a)
stack = []
stack.append(start)
cnt = 1
def dfs(pp):
    global cnt
    visit[pp] = cnt
    matrix[pp].sort(reverse=True)
    for i in matrix[pp]:
        if not visit[i]:
            cnt += 1
            dfs(i)
dfs(start)
for i in range(1, N+1):
    print(visit[i])