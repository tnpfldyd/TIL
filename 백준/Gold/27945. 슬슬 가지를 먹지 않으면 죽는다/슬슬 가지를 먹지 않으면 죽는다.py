import sys
input = sys.stdin.readline

def find(x):
    if parents[x] == x:
        return x
    parents[x] = find(parents[x])
    return parents[x]

def union(a, b):
    if a < b:
        b, a = a, b
    parents[a] = b

N, M = map(int, input().split())
parents = [i for i in range(N + 1)]
edges = sorted([tuple(map(int, input().split())) for _ in range(M)], key=lambda x : x[2])
day = 1
for a, b, d in edges:
    if d != day:
        break
    a, b = find(a), find(b)
    if a != b:
        union(a, b)
        day += 1

print(day)