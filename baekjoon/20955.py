import sys
input = sys.stdin.readline

N, M = map(int, input().split())
parent = list(range(N + 1))
result = 0

def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x, y = find(x), find(y)
    if x == y:
        return False
    if x > y:
        y, x = x, y
    parent[x] = y
    return True

for _ in range(M):
    a, b = map(int, input().split())
    if not union(a, b):
        result += 1

for i in range(1, N):
    if union(i, i + 1):
        result += 1

print(result)