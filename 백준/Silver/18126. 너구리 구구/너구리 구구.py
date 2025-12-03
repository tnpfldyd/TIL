import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

n = int(input())
g = [[] for _ in range(n+1)]
for _ in range(n-1):
    a,b,c = map(int, input().split())
    g[a].append((b,c))
    g[b].append((a,c))

mx = 0

def dfs(x, p, d):
    global mx
    if d > mx: mx = d
    for y,c in g[x]:
        if y != p:
            dfs(y, x, d + c)

dfs(1, 0, 0)
print(mx)