import sys
input = sys.stdin.readline
N, M = map(int,input().split())
result = []
def dfs(cnt):
    if cnt == M:
        print(*result)
        return
    for i in range(1, N + 1):
        result.append(i)
        dfs(cnt + 1)
        result.pop()
dfs(0)