import sys
input = sys.stdin.readline

T = int(input())

def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    px, py = find(x), find(y)
    if px != py:
        parent[px] = py

for i in range(1, T + 1):
    N, K = int(input()), int(input())
    parent = [i for i in range(N + 1)]
    for _ in range(K):
        a, b = map(int, input().split())
        union(a, b)

    print(f'Scenario {i}:')
    M = int(input())
    for _ in range(M):
        a, b = map(int, input().split())
        print(1 if find(a) == find(b) else 0)
    print()
