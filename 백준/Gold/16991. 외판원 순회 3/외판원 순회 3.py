import sys
input = sys.stdin.readline
INF = sys.maxsize

N = int(input())
matrix = [[0] * N for _ in range(N)]
visited = [[-1] * (1 << N) for _ in range(N)]
nodes = []
for _ in range(N):
    a, b = map(int, input().split())
    nodes.append((a, b))

for i in range(N-1):
    for j in range(i+1, N):
        cost = ((nodes[i][0] - nodes[j][0]) ** 2 + (nodes[i][1] - nodes[j][1]) ** 2) ** 0.5
        matrix[i][j] = cost
        matrix[j][i] = cost

def dfs(node, bit):
    if bit == (1 << N) - 1:
        return matrix[node][0] or INF
    
    if visited[node][bit] != -1:
        return visited[node][bit]
    
    dist = INF
    for i in range(1, N):
        if matrix[node][i] and not (bit & 1 << i):
            dist = min(dist, dfs(i, bit | 1 << i) + matrix[node][i])
    visited[node][bit] = dist
    return visited[node][bit]

print(dfs(0, 1))