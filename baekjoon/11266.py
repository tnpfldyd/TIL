import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
N, M = map(int, input().split())
matrix = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    matrix[a].append(b)
    matrix[b].append(a)

def dfs(x, root):
    global cnt
    cnt += 1
    visited[x] = cnt
    ret = visited[x]
    child = 0
    for i in matrix[x]:
        if visited[i]:
            ret = min(ret, visited[i])
        else:
            child += 1
            prev = dfs(i, False)
            if not root and prev >= visited[x]:
                answer[x] = True
            ret = min(ret, prev)
    if root and child > 1:
        answer[x] = True
    return ret

visited = [0] * (N + 1)
answer = [False] * (N + 1)
cnt = 0
for i in range(1, N + 1):
    if not visited[i]:
        dfs(i, True)
result = []
for i in range(1, N + 1):
    if answer[i]:
        result.append(i)
print(len(result))
print(*result)
