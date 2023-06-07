from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
matrix = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    matrix[a].append(b)
    matrix[b].append(a)

visited = [False] * (N + 1)
visited[1] = True
depth = [0] * (N + 1)
parent = [0] * (N + 1)
q = deque()
q.append(1)

while q:
    x = q.popleft()
    for nx in matrix[x]:
        if not visited[nx]:
            depth[nx] = depth[x] + 1
            visited[nx] = True
            parent[nx] = x
            q.append(nx)

M = int(input())

def LCA(x, y):
    if depth[x] > depth[y]:
        x, y = y, x
    while depth[x] != depth[y]:
        y = parent[y]
    while x != y:
        x, y = parent[x], parent[y]
    return x

for _ in range(M):
    a, b = map(int, input().split())
    print(LCA(a, b))