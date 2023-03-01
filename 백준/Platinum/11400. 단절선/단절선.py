import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
N, M = map(int, input().split())
matrix = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    matrix[a].append(b)
    matrix[b].append(a)

visited = [0] * (N + 1)
cnt = 0
answer = []

def dfs(node, eve):
    global cnt
    cnt += 1
    visited[node] = cnt
    ret = visited[node]
    for next in matrix[node]:
        if next == eve:
            continue
        if not visited[next]:
            prev = dfs(next, node)
            if prev > visited[node]:
                if next > node:
                    answer.append((node, next))
                else:
                    answer.append((next, node))
            ret = min(ret, prev)
        else:
            ret = min(ret, visited[next])
    return ret
    
for i in range(1, N + 1):
    if not visited[i]:
        dfs(i, 0)
answer.sort()
print(len(answer))
for i in answer:
    print(*i)