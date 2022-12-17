import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
N = int(input())
matrix = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(int, input().split())
    a -= 1; b -= 1
    matrix[a].append(b)
    matrix[b].append(a)
visited = [False] * N
visited[0] = True
temp, result = 0, 0
def dfs(node, cnt):
    global result, temp
    if cnt > result:
        temp = node
        result = cnt
    for i in matrix[node]:
        if not visited[i]:
            visited[i] = True
            dfs(i, cnt+1)
dfs(0, 0)
result = 0
visited = [False] * N
visited[temp] = True
dfs(temp, 0)
if result % 2:
    print(result//2 + 1)
else:
    print(result//2)