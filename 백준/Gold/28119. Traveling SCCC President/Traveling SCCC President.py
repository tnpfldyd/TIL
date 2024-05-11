import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)
N, M, S = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(M)]
loads = list(map(int, input().split()))
edges.sort(key=lambda x : x[2])
parents = [i for i in range(N + 1)]

def find(x):
    if x == parents[x]:
        return x
    parents[x] = find(parents[x])
    return parents[x]

def union(x, y):
    if x < y:
        y, x = x, y
    parents[x] = y
    
result = cnt = 0
for a, b, c in edges:
    x, y = find(a), find(b)
    if x != y:
        union(x, y)
        result += c
        cnt += 1
    if N - 1 == cnt:
        break
    
print(result)