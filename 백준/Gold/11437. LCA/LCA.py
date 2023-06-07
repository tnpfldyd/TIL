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
answer = {}

while q:
    x = q.popleft()
    for nx in matrix[x]:
        if not visited[nx]:
            depth[nx] = depth[x] + 1
            visited[nx] = True
            parent[nx] = x
            q.append(nx)

M = int(input())

def lca(a, b):    
    if a > b: 
        a, b = b, a
    x, y = a, b
        
    if (a, b) in answer:
        return answer[(a, b)]
    
    if depth[a] > depth[b]:
        a, b = b, a
    
    while depth[a] != depth[b]:
        b = parent[b]
    while a != b:
        a, b = parent[a], parent[b]
    
    answer[(x, y)] = a
    return a   

for _ in range(M):
    a, b = map(int, input().split())
    print(lca(a, b))