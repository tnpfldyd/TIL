import sys
input = sys.stdin.readline
N, M = map(int,input().split())
result = []
visited = [False] * (N + 1)
def dfs(num):
    if num == M:
        print(*result)
        return
    for i in range(1, N + 1):
        if not visited[i]:
            visited[i] = True
            result.append(i)
            dfs(num + 1)
            result.pop()
            visited[i] = False
dfs(0)