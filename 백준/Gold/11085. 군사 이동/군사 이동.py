import sys
input = sys.stdin.readline
N, M = map(int, input().split())
S, E = map(int, input().split())

edges = sorted([tuple(map(int, input().split())) for _ in range(M)], key=lambda x : -x[2])
parents = [i for i in range(N)]
def find(x):
    if x == parents[x]:
        return x
    parents[x] = find(parents[x])
    return parents[x]

def union(x, y):
    x, y = find(x), find(y)
    if x < y:
        x, y = y, x
    parents[x] = y
    
for a, b, c in edges:
    union(a, b)
    if find(S) == find(E):
        print(c)
        break
