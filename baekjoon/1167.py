import sys
input = sys.stdin.readline
N = int(input())
matrix = [[] for _ in range(N)]
for i in range(N):
    num = list(map(int, input().strip().split()))
    for j in range(1, len(num), 2):
        if num[j] != -1:
            matrix[num[0]-1].append((num[j+1], num[j]-1))

visited = [-1] * N
visited[0] = 0
cnt = [0, 0]
def dfs(x):
    for k, v in matrix[x]:
        nx = k + visited[x]
        if visited[v] == -1:
            visited[v] = nx
            if nx > cnt[0]:
                cnt[0] = nx; cnt[1] = v
            dfs(v)
dfs(0)
visited = [-1] * N
visited[cnt[1]] = 0
dfs(cnt[1])
print(cnt[0])