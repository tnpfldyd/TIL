import sys
input = sys.stdin.readline
N, M = map(int,input().split())
result = []
visited = [False] * (N + 1)
def dfs(num, cnt):
    if cnt == M:
        print(*result)
        return
    for i in range(num, N + 1):
        if not visited[i]:
            visited[i] = True
            result.append(i)
            dfs(i + 1, cnt + 1)
            result.pop()
            visited[i] = False
dfs(1, 0)