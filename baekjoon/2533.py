import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)
N = int(input())

graph = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (N + 1)
dp = [[0] * (N + 1) for _ in range(2)]

def find(x):
    visited[x] = True
    dp[0][x] = 1
    for nxt in graph[x]:
        if not visited[nxt]:
            find(nxt)
            dp[1][x] += dp[0][nxt]
            dp[0][x] += min(dp[0][nxt], dp[1][nxt])

find(1)
print(min(dp[0][1], dp[1][1]))