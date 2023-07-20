import sys
input = sys.stdin.readline
# sys.setrecursionlimit(10 ** 6)
MAX = 1000001
def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    if x > y:
        x, y = y, x
    parent[y] = x
    parts[x] += parts[y]
    parts[y] = 0

N = int(input())
parent = [i for i in range(MAX)]
parts = [1] * MAX

for _ in range(N):
    order, *ab = list(input().split())
    ab = map(int, ab)
    if order == 'I':
        a, b = ab
        a, b = find(a), find(b)
        if a != b:
            union(a, b)
    else:
        x = find(*ab)
        print(parts[x])

