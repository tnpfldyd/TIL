import sys
input = sys.stdin.readline

def find(parent, x):
    if x == parent[x]:
        return x
    parent[x] = find(parent, parent[x])
    return parent[x]

def union(a, b):
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

N = int(input())
parent = [0] * (N+1)
for i in range(N+1):
    parent[i] = i
X, Y, Z = [],[],[]
edges = []
for i in range(1, N+1):
    x, y, z = map(int, input().split())
    X.append((x, i)); Y.append((y, i)); Z.append((z, i))
X.sort(); Y.sort(); Z.sort()
for i in range(N-1):
    edges.append((abs(X[i][0]-X[i+1][0]), X[i][1], X[i+1][1]))
    edges.append((abs(Y[i][0]-Y[i+1][0]), Y[i][1], Y[i+1][1]))
    edges.append((abs(Z[i][0]-Z[i+1][0]), Z[i][1], Z[i+1][1]))
edges.sort()
result = 0
for cost, x, y in edges:
    x = find(parent, x); y = find(parent, y)
    if x != y:
        union(x, y)
        result += cost
print(result)